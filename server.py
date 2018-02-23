
# TODO: Simulate enemies, effects, and checks to see the changed scores
# TODO: Add rest endpoints for editing the character
# TODO: Save the character (for now) and eventually the party
# TODO: Allow creating a new character
# TODO: Add a party system that handles multiple characters, players being able to own multiple characters (representing companions)

from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
from urlparse import urlparse
from urlparse import parse_qs
import os
import json
import traceback
import sys
import MySQLdb

import queries

PORT = int(sys.argv[1])
HOST = sys.argv[2]
USER = sys.argv[3]
PASS = sys.argv[4]
DB = sys.argv[5]
WEBROOT = 'web'
INDEXFILE = WEBROOT + '/index.html'

database = MySQLdb.connect(host=HOST,
                           user=USER,
                           passwd=PASS,
                           db=DB)
cur = database.cursor()


def GetContentType(fn):
    if fn.find('.html') > -1:
        return 'text/html'
    elif fn.find('.css') > -1:
        return 'text/css'
    elif fn.find('.json') > -1:
        return 'application/json'
    else:
        return '.text'


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsedParams = urlparse(self.path)
        fn = WEBROOT + parsedParams.path
        if fn == 'web/':
            self.ServeIndex()
        elif os.access(fn, os.R_OK):
            self.ServeFile(fn)
        elif fn.startswith('web/calendar'):
            self.ServeQuery(queries.GetCalendar)
        elif fn.startswith('web/units'):
            self.ServeQuery(queries.GetUnits)
        elif fn.startswith('web/recipes'):
            self.ServeQuery(queries.GetRecipes)
        elif fn.startswith('web/ingredients'):
            self.ServeQuery(queries.GetIngredients)
        else:
            self.Failure("Could not parse request")

    def do_POST(self):
        parsedParams = urlparse(self.path)
        query = parsedParams.path
        params = parse_qs(parsedParams.query)

    def Success(self, s=""):
        self.send_response(200)
        self.wfile.write(s)

    def Failure(self, s=""):
        print s
        self.send_response(404)
        self.end_headers()
        self.wfile.write(str(traceback.format_exc()))

    def ServeIndex(self):
        self.ServeFile(INDEXFILE)

    def ServeFile(self, fn):
        self.send_response(200)
        self.send_header('Content-Type', GetContentType(fn))
        self.end_headers()
        with open(fn, 'r') as f:
            self.copyfile(f, self.wfile)

    def ServeQuery(self, query):
        parsedParams = urlparse(self.path)
        params = parse_qs(parsedParams.query)
        self.send_response(200)
        self.send_header('Content-Type', 'json')
        self.end_headers()
        self.wfile.write(json.dumps(query(cur, params)))

SocketServer.TCPServer.allow_reuse_address = True 
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Serving at port", PORT
httpd.serve_forever()
