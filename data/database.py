from peewee import SqliteDatabase, PostgresqlDatabase

from data.config import DATABASE_URI


class Database:
    def __init__(self, name='db.sqlite3'):
        # self.database_connect = PostgresqlDatabase(DATABASE_URI)
        self.database_connect = SqliteDatabase(name)
        self.database_connect.connect()

