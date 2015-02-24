__author__ = 'nikitaprianichnikov'
from peewee import *
import config
import datetime
from urlparse import urlparse

db = SqliteDatabase(config.database)


def create_tables():
    db.create_tables([Record])


class BaseModel(Model):
    class Meta:
        database = db


class Record(BaseModel):
    name = CharField()
    description = CharField()
    url = CharField()
    faviconUrl = CharField()
    createdAt = DateTimeField(default=datetime.datetime.now)
    tags = CharField()


    def tags_list(self):
        return self.tags.split(",")

    def host(self):
        return urlparse(self.url).netloc


    def pretty_time(self):
        return self.createdAt.strftime('%Y-%m-%d %H:%M')
