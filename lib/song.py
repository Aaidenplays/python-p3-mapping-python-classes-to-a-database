# import sys
# __package__ = 'lib'
# sys.path[0] = '/home/aaiden/code/labs/phase-3/python-p3-mapping-python-classes-to-a-database'
from __init__ import CURSOR
import ipdb 

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        
        ipdb.set_trace()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]


    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song