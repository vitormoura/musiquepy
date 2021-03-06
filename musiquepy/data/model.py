from sqlalchemy import Boolean, Column, Integer, String, BLOB
from sqlalchemy.orm import declarative_base, relationship
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
    serialize_rules = ('-password',)

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
    serialize_rules = ('-genres.artists',)

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

class AlbumPhoto(Base):
    __tablename__ = 'CAD_ALBUM_PHOTO'

    id = Column('SEQ_ALBUM_PHOTO', Integer, autoincrement=True, primary_key=True)
    album_id = Column('SEQ_ALBUM', Integer, ForeignKey(Album.id))
    content_type = Column('DSC_MIME_TYPE', String(255))
    size = Column('NUM_TAILLE', Integer)
    compressed = Column('FLG_COMPRESSE', Integer)
    content = Column('BIN_ALBUM_PHOTO', BLOB)
    

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
