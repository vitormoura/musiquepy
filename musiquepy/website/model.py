from datetime import time, timedelta
from sqlite3.dbapi2 import IntegrityError
from typing import List


class GenericRecord:
    def __init__(self, id, description: str) -> None:
        self.id = id
        self.description = description


class Album(GenericRecord):
    def __init__(self) -> None:
        super()
        self.artist = None


class User:
    def __init__(self) -> None:
        self.id = 0
        self.mail = None
        self.name = None
        self.password = None


class MusicTrack:
    def __init__(self) -> None:
        self.id = 0
        self.name = ''
        self.order = -1
        self.album = None
        self.artist = None
        self.duration = timedelta()


class MusicTracksViewModel:
    def __init__(self, tracks: List[MusicTrack]):
        self.tracks = tracks

    def length(self):
        return len(self.tracks)

    def get_tracks(self):
        return self.tracks

    def get_albums(self) -> List[GenericRecord]:
        albums = dict()

        for track in self.tracks:
            if track.album and track.album.id not in albums:
                albums[track.album.id] = track.album

        return albums.values()

    def get_tracks_by_album(self, album_id) -> List[MusicTrack]:
        return filter(lambda t: t.album.id == album_id, self.tracks)
