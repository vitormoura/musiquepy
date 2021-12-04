import os

from sqlalchemy import create_engine
from musiquepy.data.db import MusiquepyDB


def get_musiquepy_db() -> MusiquepyDB:
    """Récupère un nouvel objet MusiquepyDB (utilise SQLAlchemy)"""

    dir = os.path.dirname(__file__)
    db_path = os.path.join(dir, 'musiquepy_db.sqlite')

    engine = create_engine("sqlite+pysqlite:///" +
                           db_path, echo=True, future=True)

    return MusiquepyDB(engine)
