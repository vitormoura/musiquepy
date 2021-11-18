import os
from .musiquepy_db import MusiquepyDB

from flask.helpers import get_root_path


def get_musiquepy_db() -> MusiquepyDB:
    """Récupère un nouvel objet MusiquepyDB"""

    db_path = os.path.join(get_root_path('app'), 'data/musiquepy_db.sqlite')

    return MusiquepyDB(db_path)
