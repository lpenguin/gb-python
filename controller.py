# -*- coding: utf-8 -*-
__author__ = 'nikitaprianichnikov'
from itertools import imap, chain
import json
from models import *


def add_link(link):
    Record.create(name=link['name'],
                  description=link['description'],
                  url=link['url'],
                  faviconUrl=link['url'],
                  tags=','.join(link['tags']))


def remove_link(record_id):
    record = Record.get(id=record_id)
    record.delete_instance()


def identity(x): return x


def get_records():
    def encode(record):
        record.name = record.name.encode('ascii', 'ignore')
        record.tags = '' #record.tags.encode('utf-8')
        record.description = '' #record.description.encode('utf-8')
        return record

    return imap(encode , Record.select())


def tags():
    return flatten(imap(lambda r: r.tags_list(), Record.select()))


def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))