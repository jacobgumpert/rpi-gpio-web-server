from CGI_Handler import g_CGIHandler

import json

class DEMO_cgi():
    def __init__(self):
        self.name = 'data'

        self.register_cgi()

    def print_data(self, data):
            print json.dumps(data, indent = 4)


    def register_cgi(self):
        print g_CGIHandler.getName()
        g_CGIHandler.register( self.name, self.print_data)


