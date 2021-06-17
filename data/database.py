import sqlite3
import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from data.config import DATABASE_URI


class Database:
    def __init__(self):
        # self.connection = psycopg2.connect(DATABASE_URI)
        # self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        create_table_query = '''CREATE TABLE IF NOT EXISTS users(
                                    uid INT PRIMARY KEY NOT NULL,
                                    name TEXT NOT NULL);'''
        self.cursor.execute(create_table_query)
        self.connection.commit()

