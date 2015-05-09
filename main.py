import myExtendedSimpleServer
from CGI_Handler import g_CGIHandler
from demo_cgi import DEMO_cgi


if __name__ == '__main__':
    demo = DEMO_cgi()
    PORT = 8000
    server = myExtendedSimpleServer.createServer('localhost', PORT)

