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
import json

LOG_FILE = "log.txt"
dirname = os.path.dirname(sys.argv[0])
log = Logger(LOG_FILE)
app = Bottle()

def main():
    Database.init()
    g1 = Group(name="foobar", password="secret")
    g1.save()
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

@app.route("/ajax/register", method='POST')
def register():
    groupname  = request.forms.get("inpName")
    password   = request.forms.get("inpPassword")
    floorplans = request.files.getall("inpFloorplans") #forms.get("inpFloorplans")
    dsgvo      = request.forms.get("cbDSGVO")
    print(groupname)
    print(floorplans)

    for k in request.files:
        print("%s: %s" % (k,42))
    #print(request.files)

    validfps = [fp for fp in floorplans if os.path.splitext(fp.filename)[1] in (".png", ".jpg", ".jpeg")]
    if len(validfps) != len(floorplans):
        # at least one fp not an image
        pass

    response.content_type = 'application/json'
    return json.dumps({"message": "wer das liest ist doof"})

if __name__ == "__main__":
    main()
