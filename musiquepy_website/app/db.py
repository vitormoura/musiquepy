import logging
import os

from flask.helpers import get_root_path

from datetime import datetime
from sqlite3 import Row, Connection, connect

from app.model import User
from app.errors import MusiquepyExistingUserError


class MusiquepyDB:
    _db_file: str = ""
    _conn: Connection = None

    def __init__(self, database: str) -> None:
        self._db_file = database
        self._conn = None
        self._log = logging.getLogger(__name__)

    def connect(self):
        self._conn = connect(self._db_file)
        self._conn.row_factory = Row

    def close(self):
        self._conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_user_by_email(self, mail: str) -> User:
        cur = self._conn.cursor()
        cur.execute(
            'SELECT * FROM CAD_UTILISATEURS WHERE TXT_COURRIEL = ?', [mail])
        result = cur.fetchone()

        if result is None:
            logging.debug('user not found: %s', mail)
            return None

        usr = User()
        usr.mail = result['TXT_COURRIEL']
        usr.id = result['SEQ_UTILISATEUR']
        usr.name = result['NOM_UTILISATEUR']
        usr.password = result['TXT_MOT_PASSE']

        return usr

    def create_user(self, name: str, email: str, password: str) -> User:
        usr = self.get_user_by_email(email)

        if usr is not None:
            raise MusiquepyExistingUserError(
                f"utilisateur existe déjà: {email}")

        cur = self._conn.cursor()
        cur.execute('INSERT INTO CAD_UTILISATEURS (TXT_COURRIEL, TXT_MOT_PASSE, NOM_UTILISATEUR, FLG_ACCEPTE_MARKETING, FLG_ACTIF, DTH_ENREGISTR, DTH_CONF_COURRIEL) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (email, password, name, 0, 1, datetime.now(), None))

        self._conn.commit()

        user = User()
        user.name = name
        user.mail = email

        return user

    def get_genres(self):
        cur = self._conn.cursor()
        return [{'id': id, 'description': desc} for (id, desc) in cur.execute('SELECT * FROM TAB_GENRES ORDER BY DSC_GENRE')]

    def get_genre_by_id(self, id: int) -> dict:
        cur = self._conn.cursor()
        result = cur.execute(
            'SELECT * FROM TAB_GENRES WHERE COD_GENRE = ? ORDER BY DSC_GENRE', [id]).fetchone()

        if result is None:
            return None

        id, description = result

        return {'id': id, 'description': description}

def get_musiquepy_db() -> MusiquepyDB:
    """Récupère un nouvel objet MusiquepyDB"""

    db_path = os.path.join(get_root_path('app'), 'musiquepy_db.sqlite')

    return MusiquepyDB(db_path)
