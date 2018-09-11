# -*- coding: utf-8 -*-

from bottle import Bottle, run, \
     template, debug, static_file, \
     request, response, redirect

from util import Logger
from models import *

import os, sys
import datetime
import time
import datetime
import atexit

LOG_FILE = "log.txt"
dirname = os.path.dirname(sys.argv[0])
log = Logger(LOG_FILE)
app = Bottle()

def main():
    atexit.register(stop)
    debug(True) 
    run(app, host="localhost", port = 8080)   

def stop():
    log.close()
    Database.instance.close()

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

@app.route('/registration')
def register():
    return template("registration", data = params())

@app.route('/')
def index():
    return template("index", data = params())

if __name__ == "__main__":
    main()
