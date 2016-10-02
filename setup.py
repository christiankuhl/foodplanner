#!/usr/bin/python

import sys
import json
from subprocess import call
import os

try:
    with open('setup.conf','r') as configfile:
        config = json.load(configfile)
    try:
        arg = sys.argv[1]
    except:
        print "Please enter a valid project configuration. Available\
         configurations are:\n%s" % \
            ', '.join(config.keys())
    if arg in config.keys():
        config = config[arg]
        print "Entering project configuration %s...\n" % arg
        print "Creating app.conf..."
        with open('kivy/app.conf','wb') as appconfig:
            json.dump(config,appconfig)
        if config["deploy_server"]:
            try:
                retcode = call("scp -r " + os.path.dirname(os.path.abspath(__file__))
                               + " " + config["server"] + ":" + config["path"])
                if retcode < 0:
                    print >>sys.stderr, "Copying aborted."
                else:
                    print >>sys.stderr
            except OSError as e:
                print >>sys.stderr, "Execution failed:", e
        if config["run_server"]:
            print "Starting server app...\n"
        if config["run_app"]:
            print "Starting client app locally...\n"
        if config["deploy_android"]:
            print "Deploying onto Android...\n"
        if config["deploy_iOS"]:
            print "Deploying onto iOS...\n"

    else:
        print "Unknown configuration. Available configurations are:\n%s" % \
            ', '.join(config.keys())

except Exception as e:
    print e
    print "Fatal: Configuration file setup.conf not found!"
