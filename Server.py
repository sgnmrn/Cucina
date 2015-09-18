__author__ = 'marino'
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from Menu import *

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print "GET path= " +self.path
        if self.path == '/menu':
            menu = getMenu()
            self.wfile.write(menu)
        # fi = open('./Piatti','r')
        # self.wfile.write(fi.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
       # global postVars
        print "POST path= " +self.path
        self.send_response(200)
        self.end_headers()
        contLen = int(self.headers.getheader('content-length', 0))
        content = self.rfile.read(contLen)
        # Doesn't do anything with posted data
        self._set_headers()
        print content
        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

def creaMenu():
    crea("Piatti")

if __name__ == "__main__":
    from sys import argv
    creaMenu()
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()