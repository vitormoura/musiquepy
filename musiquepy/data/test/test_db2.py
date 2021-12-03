
from musiquepy.data import get_musiquepy_db2


def test__get_user_by_email():
    db = get_musiquepy_db2()
    usr = db.get_user_by_email('mail@mail.com')

    assert usr != None
    assert usr.email == 'mail@mail.com'

    usr2 = db.get_user_by_email('nonexistent@mail.com')

    assert usr2 == None


def test__get_genres():
    db = get_musiquepy_db2()
    genres = db.get_genres()

    assert genres != None
    assert len(genres) > 0


def test__get_genres_by_id():
    db = get_musiquepy_db2()
    genre = db.get_genre_by_id(30)

    assert genre != None
    assert len(genre.description) > 0
    assert genre.id == 30

    genre2 = db.get_genre_by_id(999)

    assert genre2 == None

def test__get_artist_by_id():
    db = get_musiquepy_db2()
    artist = db.get_artist_by_id(1)

    assert artist != None
    assert artist.id == 1

    artist2 = db.get_artist_by_id(999)    

    assert artist2 == None