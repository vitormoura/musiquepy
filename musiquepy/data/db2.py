
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, select
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


class MusiquepyDB2:
    _engine: Engine

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def get_users(self):
        with Session(self._engine) as session:
            session: Session
            result: ResultProxy

            result = session.execute(select(User))

            return result.scalars().fetchall()
