from CGI_Handler import g_CGIHandler
import logging

# try:
import RPi.GPIO as GPIO
import json



#setup GPIO using Board numbering

GPIO.setmode(GPIO.BOARD)

class GPIO_cgi():
    ''' API for GPIO 
    'action=get&channels=1,2,3'
    'action=set&1=0&3=1'
    '''
    def __init__(self):
        self.getname = 'gpio'


        self.register_cgi()


        GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(5, GPIO.OUT, initial=GPIO.HIGH)


    def handle_data(self, data):
        if (data['action'][0] == 'get'):
            return self.get_data(data)
        elif (data['action'][0] == 'set'):
            return self.set_data(data)
        else:
            return {msg: 'Unknown action'}

    def get_data(self, data):
        print json.dumps(data, indent = 4)
        resp = {}
        channels = data['channels'][0].split(',')
        for channel in channels:
            print channel
            resp[channel] = GPIO.input(int(channel))
        return resp


    def set_data(self, data):
        print json.dumps(data, indent = 4)
        resp = {}
        channel = int(data['channel'][0])
        status = int(data['status'][0])
        gpio_status = GPIO.HIGH if status == 1 else GPIO.LOW
        print channel, status
        resp[channel] = GPIO.output(int(channel), gpio_status)
        return resp

    def register_cgi(self):
        # g_CGIHandler.registerCallBack( self.setname, self.set_data)
        g_CGIHandler.registerCallBack( self.getname, self.handle_data)

# except:
#     logging.error('Could not get RPi.GPIO')
#     class GPIO_cgi():
#         def __init__(self):
#             self.getname = 'gpio-get'
#             self.setname = 'gpio-set'
#             self.register_cgi()


#         def handle_data(self, data):
#             print json.dumps(data, indent = 4)
#             return {'msg':'gpio'}


#         def register_cgi(self):
#             g_CGIHandler.registerCallBack( self.getname, self.handle_data)
#             g_CGIHandler.registerCallBack( self.setname, self.handle_data)
