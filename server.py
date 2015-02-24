# -*- coding: UTF-8 -*-

__author__ = 'nikitaprianichnikov'
from bottle import Bottle, request, static_file, response
from bottle_jade import JadePlugin
from os import path as op
import json

import controller
import config

templates = op.join(op.dirname(op.abspath(__file__)), 'views')
app = Bottle()
jade = app.install(JadePlugin(template_folder=templates))


@app.route('/api/addLink', method='POST')
def add_link():
    data = request.body.readline()
    link = json.loads(data)
    controller.add_link(link)
    return dict(status='ok')


@app.route('/api/tags', method='GET')
def tags():
    response.headers['Content-Type'] = 'application/json'
    tags_list = controller.tags()
    return json.dumps(dict(status='ok', result=tags_list))


@app.route('/', method='GET')
@jade.view('index.jade')
def index():
    return {'items': controller.get_records()}


@app.route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root=config.static_root)


app.run(host='localhost', port=8080, debug=True, reloader=True)




