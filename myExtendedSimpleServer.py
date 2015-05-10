from CGI_Handler import g_CGIHandler


import SimpleHTTPServer
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer
import logging
import cgi
from SocketServer import ThreadingMixIn
import threading
import os
import json


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def handleCGI(self):
        path_list = self.path.split('?')
        if(len(path_list) == 2):

            cgi_string = os.path.basename(path_list[0])
            data_string = path_list[1]
            in_d = cgi.parse_qs(data_string)

            message = g_CGIHandler.callCGI(cgi_string, in_d)

            if not message:
                message = '{ "msg": "Could Not find cgi"}'
                response = 400

            else:
                response = 200
                message = json.dumps(message)
            logging.error("response msg: %s (%d)"%(message, response))

        else:
            message =  threading.currentThread().getName()
            response = 400

        self.send_response(response)
        self.end_headers()

        self.wfile.write(message)
        self.wfile.write('\n')

        return


    def do_GET(self):
        logging.error(self.headers)
        self.path = 'html' + self.path
        logging.error("Test path is: " + self.path)
        if (os.path.exists(self.path)):
            useSimple = True
        elif (os.path.exists(self.path.split('?')[0])) :
            useSimple = True
        else : 
            useSimple = False

        if (useSimple):
            print('Using simple HTTPServer')
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:        
            self.handleCGI()


    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def createServer(host, port):
    server = ThreadedHTTPServer((host, port), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
    return server


if __name__ == '__main__':
    PORT = 8000
    createServer('localhost', PORT)
