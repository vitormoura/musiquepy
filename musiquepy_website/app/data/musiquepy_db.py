import sqlite3


class MusiquepyDB:
    _db_file: str = ""
    _conn: sqlite3.Connection = None

    def __init__(self, database: str) -> None:
        self._db_file = database
        self._conn = None

    def connect(self):
        self._conn = sqlite3.connect(self._db_file)

    def close(self):
        self._conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_genres(self):
        cur = self._conn.cursor()
        return [{'id': id, 'description': desc} for (id, desc) in cur.execute('SELECT * FROM TAB_GENRES ORDER BY DSC_GENRE')]

    def get_genre_by_id(self, id: int) -> dict:
        cur = self._conn.cursor()
        result = cur.execute(
            'SELECT * FROM TAB_GENRES WHERE COD_GENRE = ? ORDER BY DSC_GENRE', [id]).fetchone()

        if result is None:
            return None

        id, description = result

        return {'id': id, 'description': description}        
