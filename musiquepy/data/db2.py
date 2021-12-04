
from datetime import datetime
from typing import List

from sqlalchemy.sql.expression import false
from musiquepy.data.errors import MusiquepyExistingUserError

from musiquepy.data.model import Album
from sqlalchemy import Boolean, Column, Integer, String, select
from sqlalchemy.engine import Engine, ResultProxy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()


MusicGenreArtistsRel = Table('CAD_GENRE_MUSIQ_ARTISTE', Base.metadata,
                             Column('COD_GENRE_MUSIQ', ForeignKey(
                                 'TAB_GENRES_MUSIQ.COD_GENRE_MUSIQ')),
                             Column('COD_ARTISTE', ForeignKey(
                                 'CAD_ARTISTES.SEQ_ARTISTE'))
                             )


class User(Base, SerializerMixin):
    __tablename__ = 'CAD_UTILISATEURS'

    id = Column(Integer, name='SEQ_UTILISATEUR',
                primary_key=True, autoincrement=True)
    email = Column(String(256), name='TXT_COURRIEL')
    password = Column(String(256), name='TXT_MOT_PASSE')
    name = Column(String(1024), name='NOM_UTILISATEUR')
    accept_marketing = Column(Boolean, name="FLG_ACCEPTE_MARKETING")
    active = Column(Boolean, name="FLG_ACTIF")
    created_at = Column(Integer, name="DTH_ENREGISTR")
    email_confirmed_at = Column(Integer, name="DTH_CONF_COURRIEL")


class MusicGenre(Base, SerializerMixin):
    __tablename__ = 'TAB_GENRES_MUSIQ'

    id = Column(Integer, name='COD_GENRE_MUSIQ', primary_key=True)
    description = Column(String(255), name='DSC_GENRE_MUSIQ')

    artists = relationship(
        'Artist', secondary=MusicGenreArtistsRel, back_populates='genres')


class Artist(Base, SerializerMixin):
    __tablename__ = 'CAD_ARTISTES'

    id = Column('SEQ_ARTISTE', Integer, autoincrement=True, primary_key=True)
    name = Column('NOM_ARTISTE', String(255))
    code = Column('COD_ARTISTE', String(128))
    country = Column('COD_PAYS_ORIGINE', Integer)
    year_activity_start = Column('NUM_ANNEE_DEBUT_ACTIVITE', Integer)
    year_activity_end = Column(
        'NUM_ANNEE_FIN_ACTIVITE', Integer, nullable=True)
    website = Column('URL_SITEWEB', String(1024))
    history = Column('DSC_HISTORIQUE', String(2048))

    genres = relationship(
        'MusicGenre', secondary=MusicGenreArtistsRel, back_populates='artists')


"""
-- CAD_ALBUM definition

CREATE TABLE CAD_ALBUM (
    SEQ_ALBUM           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    COD_TYPE_ALBUM      INTEGER NOT NULL,
    COD_ALBUM           TEXT(32) NOT NULL, -- GUID
    SEQ_ARTISTE         INTEGER NOT NULL,
    NOM_ALBUM           TEXT(255) NOT NULL,
    NUM_ANNEE_SORTIE    INTEGER NOT NULL,
    DSC_ALBUM           TEXT(1024)
);
"""


class Album(Base, SerializerMixin):
    __tablename__ = 'CAD_ALBUM'

    id = Column('SEQ_ALBUM', Integer, autoincrement=True, primary_key=True)
    type = Column('COD_TYPE_ALBUM', Integer)
    code = Column('COD_ALBUM', String(32))
    artist_id = Column('SEQ_ARTISTE', Integer, ForeignKey(Artist.id))
    name = Column('NOM_ALBUM', String(255))
    year = Column('NUM_ANNEE_SORTIE', Integer)
    description = Column('DSC_ALBUM', String(1024))

    artist = relationship(Artist)
    tracks = relationship('MusicTrack', back_populates='album')


class MusicTrack(Base, SerializerMixin):
    serialize_rules = ('-album.tracks', '-album.artist.genres')

    __tablename__ = "CAD_PISTES_ALBUM"

    id = Column('SEQ_PISTE', Integer, primary_key=True, autoincrement=True)
    music_id = Column('SEQ_CHANSON', Integer, nullable=True)
    album_id = Column('SEQ_ALBUM', Integer, ForeignKey(Album.id))
    order = Column('NUM_ORDRE', Integer)
    side = Column('NUM_FACE', Integer)
    name = Column('NOM_PISTE', String(255))
    duration = Column('NUM_DURATION_SEC', Integer)

    album = relationship(Album, back_populates='tracks')


class MusiquepyDB2:
    _engine: Engine

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def create_user(self, name: str, email: str, password: str) -> User:
        usr = self.get_user_by_email(email)
                
        if usr is not None:
            raise MusiquepyExistingUserError(
                f"utilisateur existe déjà: {email}")
        
        with Session(self._engine) as session:
            session: Session
            session.expire_on_commit = False

            usr = User()
            usr.email = email
            usr.name = name
            usr.password = password
            usr.accept_marketing = 0
            usr.active = 1
            usr.created_at = int(datetime.now().timestamp())
            usr.email_confirmed_at = None
            
            session.add(usr)
            session.commit()                        
        
        return usr

    def get_users(self) -> List[User]:
        with Session(self._engine) as session:
            session: Session
            result: ResultProxy

            result = session.execute(select(User))

            return [row.User for row in result.fetchall()]

    def get_user_by_email(self, email) -> User:
        with Session(self._engine) as session:
            session: Session

            stmt = select(User).where(User.email == email)

            return session.execute(stmt).scalar()

    def get_genres(self) -> List[MusicGenre]:
        with Session(self._engine) as session:
            session: Session

            stmt = select(MusicGenre).order_by(MusicGenre.description)

            return session.execute(stmt).scalars().all()

    def get_genre_by_id(self, id: int) -> MusicGenre:
        with Session(self._engine) as session:
            session: Session

            stmt = select(MusicGenre).where(MusicGenre.id == id)

            return session.execute(stmt).scalar()

    def get_artist_by_id(self, id: int) -> Artist:
        with Session(self._engine) as session:
            session: Session
            stmt = select(Artist).where(Artist.id == id)

            return session.execute(stmt).scalar()

    def get_music_tracks_by_genre(self, id_genre: int) -> List[MusicTrack]:
        with Session(self._engine) as session:

            stmt = (
                select(MusicTrack, Artist, Album)
                .join(MusicTrack.album)
                .join(Album.artist)
                .join(Artist.genres)
                .where(MusicGenre.id == id_genre)
            )

        result = session.execute(stmt)

        return [row.MusicTrack for row in result.fetchall()]
