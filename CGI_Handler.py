import logging
class CGI_handler():
    def __init__(self):
        self.register = {}

    def register(self, path, callBack):
        self.register[path] = callBack

    def callCGI(self, path, data):
        try:
            self.register[path](data)
        except:
            logging.error('Could not find cgi')

    def getName(self):
        return "CGI_handler"


g_CGIHandler = CGI_handler()
