from typing import List
from musiquepy.data.db2 import Album, MusicTrack


class MusicTracksViewModel:
    def __init__(self, tracks: List[MusicTrack]):
        self.tracks = tracks

    def length(self):
        return len(self.tracks)

    def get_tracks(self):
        return self.tracks

    def get_albums(self) -> List[Album]:
        albums = dict()

        for track in self.tracks:
            if track.album and track.album.id not in albums:
                albums[track.album.id] = track.album

        return albums.values()

    def get_tracks_by_album(self, album_id) -> List[MusicTrack]:
        return filter(lambda t: t.album.id == album_id, self.tracks)
