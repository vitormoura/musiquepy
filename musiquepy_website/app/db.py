import logging
import os

from typing import List
from flask.helpers import get_root_path
from datetime import datetime, time, timedelta
from sqlite3 import Row, Connection, connect

from app.config import DB_FILEPATH
from app.model import Album, GenericRecord, MusicTrack, User
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
    
    def get_genres(self) -> List[GenericRecord]:
        cur = self._conn.cursor()
        return [GenericRecord(id, desc) for (id, desc) in cur.execute('SELECT * FROM TAB_GENRES ORDER BY DSC_GENRE')]

    def get_genre_by_id(self, id: int) -> GenericRecord:
        cur = self._conn.cursor()
        result = cur.execute(
            'SELECT * FROM TAB_GENRES_MUSIQ WHERE COD_GENRE_MUSIQ = ? ORDER BY DSC_GENRE_MUSIQ', [id]).fetchone()

        if result is None:
            return None

        return GenericRecord(result['COD_GENRE_MUSIQ'], result['DSC_GENRE_MUSIQ'])        

    def get_music_tracks_by_genre(self, id_genre: int) -> List[MusicTrack]:
        query = """
            SELECT 
            	cpa.SEQ_PISTE,
                ca.NOM_ALBUM,
                ca.COD_ALBUM,
                ca.SEQ_ALBUM,
                cpa.NOM_PISTE,
                cpa.NUM_ORDRE,
                cpa.NUM_DURATION_SEC,
                ca2.NOM_ARTISTE,	
                ca2.COD_ARTISTE,
                ca2.SEQ_ARTISTE 
            FROM 
                CAD_PISTES_ALBUM cpa 
                INNER JOIN CAD_ALBUM ca ON ca.SEQ_ALBUM = cpa.SEQ_ALBUM
                INNER JOIN CAD_ARTISTES ca2 ON ca2.SEQ_ARTISTE = ca.SEQ_ARTISTE
                INNER JOIN CAD_GENRE_MUSIQ_ARTISTE cgma ON cgma.COD_ARTISTE = ca.SEQ_ARTISTE
            WHERE 
                cgma.COD_GENRE_MUSIQ = ?
        """

        cur = self._conn.cursor()
        result = cur.execute(query, (id_genre,))
        tracks = list()
        
        for row in result:
            track = MusicTrack()
            track.id = row['SEQ_PISTE']
            track.name = row['NOM_PISTE']
            track.duration = timedelta(seconds=row['NUM_DURATION_SEC'])
            track.order = row['NUM_ORDRE']

            track.artist = GenericRecord(row['SEQ_ARTISTE'], row['NOM_ARTISTE'])
            
            track.album = Album()
            track.album.id = row['SEQ_ALBUM']
            track.album.description = row['NOM_ALBUM']
            track.album.artist = track.artist;

            tracks.append(track)

        return tracks        


def get_musiquepy_db() -> MusiquepyDB:
    """Récupère un nouvel objet MusiquepyDB"""

    db_path = os.path.join(get_root_path('app'), DB_FILEPATH)

    return MusiquepyDB(db_path)
