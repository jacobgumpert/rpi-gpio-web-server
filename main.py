from myExtendedSimpleServer import ThreadedHTTPServer
from CGI_Handler import g_CGIHandler
from demo_cgi import DEMO_cgi


if __name__ == '__main__':
    demo = DEMO_cgi()
    demo.register_cgi(g_CGIHandler)
    PORT = 8000
    server = ThreadedHTTPServer(('localhost', PORT), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()

