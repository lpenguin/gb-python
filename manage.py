__author__ = 'nikitaprianichnikov'
from models import *
import sys
import json
import datetime

dump_name = sys.argv[1]

with open(dump_name) as f:
    records_json = json.load(f)
    for r in records_json:
        name = r['name']
        addedAt = r['addedAt']['$date']
        description = r['description']
        url = r['url']
        favicon_url = r['faviconUrl']

        tags = ','.join(r['tags'])
        Record.create(name=name,
                      createdAt = datetime.datetime.fromtimestamp(addedAt/1000),
                      description=description,
                      url=url,
                      faviconUrl=favicon_url,
                      tags=tags)
        print 'Created record %s ' % name

    f.close()


