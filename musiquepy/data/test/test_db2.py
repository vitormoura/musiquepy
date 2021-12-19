import pytest
from sqlalchemy.util.langhelpers import portable_instancemethod
from musiquepy.data import get_musiquepy_db
from musiquepy.data.db import MusicTrack

def test__get_genres():
    with get_musiquepy_db() as db:
        genres = db.get_genres()

        assert genres != None
        assert len(genres) > 0


def test__create_create_user():
    with get_musiquepy_db() as db:
        usr = db.create_user(
            'king arthur', 'king_arthur@camelot.com', '123456')

        assert usr is not None
        assert usr.id > 0


def test__get_user_by_email():
    with get_musiquepy_db() as db:
        usr = db.get_user_by_email('mail@mail.com')

        assert usr != None
        assert usr.email == 'mail@mail.com'

        usr2 = db.get_user_by_email('nonexistent@mail.com')

        assert usr2 == None


def test__get_genres_by_id():
    with get_musiquepy_db() as db:
        genre = db.get_genre_by_id(30)

        assert genre != None
        assert len(genre.description) > 0
        assert genre.id == 30

        genre2 = db.get_genre_by_id(999)

        assert genre2 == None


def test__get_artist_by_id():
    with get_musiquepy_db() as db:
        artist = db.get_artist_by_id(1)

        assert artist != None
        assert artist.id == 1

        artist2 = db.get_artist_by_id(999)

        assert artist2 == None


def test__get_tracks_by_id():
    with get_musiquepy_db() as db:
        tracks = db.get_music_tracks_by_genre(30)

        assert len(tracks) > 0
        assert all([isinstance(t, MusicTrack) for t in tracks])


def test__get_album_photo():
    with get_musiquepy_db() as db:
        photo = db.get_album_photo(1)

        assert photo is not None
        assert len(photo.content) > 0
