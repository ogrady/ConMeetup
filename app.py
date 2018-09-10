# -*- coding: utf-8 -*-

from bottle import Bottle, run, \
     template, debug, static_file, \
     request, response, redirect

import os, sys
import datetime
import time
import datetime

LOG_FILE = "log.txt"

class Logger(object):
    def __init__(self, filename, mode = "a"):
        self._fh = open(filename, mode)

    def error(self, message):
        self._write("ERROR", message)

    def _write(self, header, message):
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self._fh.write("[%s] %s: %s" % (header, ts, message))

dirname = os.path.dirname(sys.argv[0])
log = Logger(LOG_FILE)
app = Bottle()
debug(True)

def params(additional = {}):
    '''
    The template that wraps all subpages requires several datapoints, which are included
    (but can be overriden) as default in the data-dictionary.
    Additional parameters can be passed as dictionary for this method.
    '''
    data = {
        "year": datetime.datetime.now().year, 
        "developer_organization":"Toto",
    }
    data.update(additional)
    return data

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'static/asset/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'static/asset/js')

@app.route('/')
def index():
    return template('index', data = params())

run(app, host='localhost', port = 8080)