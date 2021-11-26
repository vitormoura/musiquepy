from datetime import timedelta

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
