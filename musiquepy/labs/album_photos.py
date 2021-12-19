import sqlite3
import os


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertAlbumPhotoBLOB(dbFilePath: str, albumId: int, photoFilePath: str):
    try:
        sqliteConnection = sqlite3.connect(dbFilePath)
        cursor = sqliteConnection.cursor()

        sqlite_insert_blob_query = """ INSERT INTO CAD_ALBUM_PHOTO
            (SEQ_ALBUM, BIN_ALBUM_PHOTO, NUM_TAILLE, DSC_MIME_TYPE, FLG_COMPRESSE)
            VALUES (?, ?, ?, ?, 0);
        """

        photo = convertToBinaryData(photoFilePath)
                
        # Convert data into tuple format
        data_tuple = (albumId, photo, len(photo), 'image/jpeg')
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()

        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


dir_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(dir_path, '..', 'data', 'musiquepy_db.sqlite')
photo_path = os.path.join(dir_path, '..', 'data',
                          'media', 'albums_pictures', 'Beatles_YellowSubmarine.jpg')

#insertAlbumPhotoBLOB(db_path, 4, photo_path)
#insertAlbumPhotoBLOB(db_path, 2, photo_path)
