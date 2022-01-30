from peewee import SqliteDatabase, PostgresqlDatabase
from pymongo import MongoClient


class Database:
    def __init__(self, postgresql=None, mongo=None, sqlite='db.sqlite3'):
        if postgresql:
            self.database_connect = PostgresqlDatabase(postgresql)
        elif mongo:
            self.database_connect = MongoClient(mongo)
        else:
            self.database_connect = SqliteDatabase(sqlite)
        self.database_connect.connect()
