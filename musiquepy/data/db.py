import io
import logging
import os
import pathlib
from datetime import datetime
from typing import List

from musiquepy.data.errors import MusiquepyExistingUserError
from musiquepy.data.media import get_profile_pictures_dir
from musiquepy.data.model import Album, Artist, MusicGenre, MusicTrack, User
from sqlalchemy import select
from sqlalchemy.engine import Engine, ResultProxy
from sqlalchemy.orm.session import Session


class MusiquepyDB:
    _engine: Engine
    _session: Session
    _log: logging.Logger

    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._log = logging.getLogger(__name__)

    def connect(self):
        self._session = Session(self._engine)
        self._session.expire_on_commit = False

    def close(self):
        self._session.close()

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

        usr = User()
        usr.email = email
        usr.name = name
        usr.password = password
        usr.accept_marketing = 0
        usr.active = 1
        usr.created_at = int(datetime.now().timestamp())
        usr.email_confirmed_at = None

        self._session.add(usr)
        self._session.commit()

        return usr

    def get_users(self) -> List[User]:

        result: ResultProxy

        result = self._session.execute(select(User))

        return [row.User for row in result.fetchall()]

    def get_user_by_id(self, id) -> User:
        stmt = select(User).where(User.id == id)

        return self._session.execute(stmt).scalar()

    def get_user_by_email(self, email) -> User:

        stmt = select(User).where(User.email == email)

        return self._session.execute(stmt).scalar()

    def get_user_profile_picture(self, user_id: int) -> io.IOBase:
        pictures_path = get_profile_pictures_dir()
        profile_pic_path = pathlib.Path(
            pictures_path, f'user_{int(user_id)}.jpg')

        if not profile_pic_path.exists():
            profile_pic_path = pathlib.Path(pictures_path, 'default.jpg')

        return io.FileIO(os.path.join(pictures_path, 'default.jpg'))

    def get_genres(self) -> List[MusicGenre]:

        stmt = select(MusicGenre).order_by(MusicGenre.description)

        return self._session.execute(stmt).scalars().all()

    def get_genre_by_id(self, id: int) -> MusicGenre:
        stmt = select(MusicGenre).where(MusicGenre.id == id)

        return self._session.execute(stmt).scalar()

    def get_artist_by_id(self, id: int) -> Artist:

        stmt = select(Artist).where(Artist.id == id)

        return self._session.execute(stmt).scalar()

    def get_music_tracks_by_genre(self, id_genre: int) -> List[MusicTrack]:

        stmt = (
            select(MusicTrack, Artist, Album)
            .join(MusicTrack.album)
            .join(Album.artist)
            .join(Artist.genres)
            .where(MusicGenre.id == id_genre)
        )

        result = self._session.execute(stmt)

        return [row.MusicTrack for row in result.fetchall()]
