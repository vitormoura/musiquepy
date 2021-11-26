import os
from musiquepy.data.db import MusiquepyDB


def get_musiquepy_db() -> MusiquepyDB:
    """Récupère un nouvel objet MusiquepyDB"""

    dir = os.path.dirname(__file__)
    db_path = os.path.join(dir, 'musiquepy_db.sqlite')

    return MusiquepyDB(db_path)
