from datetime import datetime

import peewee
from data.database import Database

import sys
import inspect

db = Database()


class BaseModel(peewee.Model):
    class Meta:
        database = db.database_connect


class User(BaseModel):

    name = peewee.CharField(max_length=50)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'users'
