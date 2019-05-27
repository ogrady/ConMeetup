# -*- coding: utf-8 -*-

from bottle import Bottle, run, \
     template, debug, static_file, \
     request, response, redirect

from util import Logger
from models import *

import datetime
import os, sys
import atexit
import json

LOG_FILE = "log.txt"
dirname = os.path.dirname(sys.argv[0])
log = Logger(LOG_FILE)
app = Bottle()

def main():
    Database.init()
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

def jsonresponse(additional = {}):
    data = {
        "message_header": "Message",
        "message": ""
    }
    data.update(additional)
    response.content_type = "application/json"
    return json.dumps(data)

@app.route("/static/<filename:re:.*\.css>")
def send_css(filename):
    return static_file(filename, root=dirname+"static/asset/css")

@app.route("/static/<filename:re:.*\.js>")
def send_js(filename):
    return static_file(filename, root=dirname+"static/asset/js")

@app.route("/registration")
def registration():
    return template("registration", data = params())

@app.route("/join")
def joining():
    return template("joining", data = params())

@app.route("/")
def index():
    return template("index", data = params())

@app.route("/ajax/join", method="POST")
def join():
    res = {}
    groupname = request.forms.get("inpGroupName").strip(' \t\n\r')
    password  = request.forms.get("inpPassword")
    username  = request.forms.get("inpUserName").strip(' \t\n\r')
    colour    = request.forms.get("inpColour")
    dsgvo     = request.forms.get("cbDSGVO")

    if User.select().join(Group, on=(User.group == Group.id)).where((User.name == username) & (Group.name == groupname) & (Group.password == password)).exists():
        with Database.instance.atomic() as transaction:
            try:
                group = Group.get(Group.name == groupname)
                user = User.get((User.name == username) & (User.group == group))
                User.colour = colour
                user.save()
            except Exception as e:
                transaction.rollback()
                log.error(str(e))
                return jsonresponse({"message": "Internal error when trying to update existing user."})

        return jsonresponse({"message": "You have been successfully logged into the group '%s'" % (groupname,)})
    elif Group.select().where(Group.name == username and Group.password == password).exists():
        with Database.instance.atomic() as transaction:
            try:
                group = Group.get(Group.name == groupname)
                user = User.create(name = username, group = group, colour = colour)
                user.save()
            except Exception as e:
                transaction.rollback()
                log.error(str(e))
                return jsonresponse({"message": "Internal error when trying to save the new user."})
        
        return jsonresponse({"message": "You have successfully joined group '%s' as '%s'" % (groupname, username,)})
    return jsonresponse({"message": "The combination of Group Name and Group Password doesn't exist."})

@app.route("/ajax/register", method="POST")
def register():
    res = {}
    groupname  = request.forms.get("inpName")
    password   = request.forms.get("inpPassword")
    floorplans = request.files.getall("inpFloorplans")
    dsgvo      = request.forms.get("cbDSGVO")

    if not all((groupname, password, floorplans, dsgvo)):
        return jsonresponse({"message": "Incomplete input."})

    validexts = (".png", ".jpg", ".jpeg")
    validfps = [fp for fp in floorplans if os.path.splitext(fp.filename)[1] in validexts]
    if len(validfps) != len(floorplans):
        return jsonresponse({"message": "Floorplans must all be of types: %s" % (str(validexts),)})

    # FIXME: remove! only for debugging!
    # Group.delete().where(Group.name == groupname).execute()

    if Group.select().where(Group.name == groupname).exists():
        return jsonresponse({"message": "Groupname '%s' is already taken, please choose another name." % (groupname,)})

    with Database.instance.atomic() as transaction:
        try:
            group = Group.create(name = groupname, password = password)
            group.save()
            for fp in validfps:
                fpm = Floorplan(group = group, filename = fp.filename)
                fpm.save()
                fp.save(fpm.filepath)
        except Exception as e:
            transaction.rollback()
            log.error(str(e))
            return jsonresponse({"message": "Internal error when trying to save the new group."})
    
    return jsonresponse({"message": "Group '%s' was successfully created." % (groupname,)})

if __name__ == "__main__":
    main()