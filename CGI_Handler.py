import logging
class CGI_handler():
    def __init__(self):
        self._register = {}

    def registerCallBack(self, path, callBack):
        self._register[path] = callBack

    def callCGI(self, path, data):
        try:
            resp = self._register[path](data)
            logging.error('Found cgi: %s'%(path))
            return  resp
        except:
            logging.error('Could not find cgi')
            return False

    def getName(self):
        return "CGI_handler"


g_CGIHandler = CGI_handler()
