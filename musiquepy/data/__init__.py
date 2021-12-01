import os

from sqlalchemy import create_engine
from musiquepy.data.db import MusiquepyDB
from musiquepy.data.db2 import MusiquepyDB2


def get_musiquepy_db() -> MusiquepyDB:
    """Récupère un nouvel objet MusiquepyDB"""

    dir = os.path.dirname(__file__)
    db_path = os.path.join(dir, 'musiquepy_db.sqlite')

    return MusiquepyDB(db_path)

def get_musiquepy_db2() -> MusiquepyDB2:
    """Récupère un nouvel objet MusiquepyDB2 (utilise SQLAlchemy)"""

    dir = os.path.dirname(__file__)
    db_path = os.path.join(dir, 'musiquepy_db.sqlite')

    engine = create_engine("sqlite+pysqlite:///" + db_path, echo=True, future=True)

    return MusiquepyDB2(engine)

    
