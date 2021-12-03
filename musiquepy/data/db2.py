
from typing import List

from sqlalchemy import Boolean, Column, Integer, String, select
from sqlalchemy.engine import Engine, ResultProxy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()


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

class Artist(Base, SerializerMixin):
    __tablename__ = 'CAD_ARTISTES'

    id = Column('SEQ_ARTISTE', Integer, autoincrement=True, primary_key=True)
    name = Column('NOM_ARTISTE', String(255))
    code = Column('COD_ARTISTE', String(128))
    country = Column('COD_PAYS_ORIGINE', Integer)
    year_activity_start = Column('NUM_ANNEE_DEBUT_ACTIVITE', Integer)
    year_activity_end = Column('NUM_ANNEE_FIN_ACTIVITE', Integer, nullable=True)
    website = Column('URL_SITEWEB', String(1024))
    history = Column('DSC_HISTORIQUE', String(2048))


class MusiquepyDB2:
    _engine: Engine

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

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
