import myExtendedSimpleServer
from CGI_Handler import g_CGIHandler
from demo_cgi import DEMO_cgi
from demo_cgi import DEMO_cgi
from gpio_cgi import GPIO_cgi

if __name__ == '__main__':
    demo = DEMO_cgi()
    gpio = GPIO_cgi()
    PORT = 8000
    try:
        import RPi.GPIO as GPIO
        server = myExtendedSimpleServer.createServer('192.168.1.72', PORT)
    except:
        server = myExtendedSimpleServer.createServer('localhost', PORT)
