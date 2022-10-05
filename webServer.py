from http.server import HTTPServer, BaseHTTPRequestHandler
from playsound import playsound
import os

ip_whitelist = [
    '127.0.0.1',
    '172.30.127.12'
]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        print(self.client_address[0])
        
        if self.client_address[0] not in ip_whitelist:
            self.wfile.write(b'Not today, bro!')
            return
        
        playsound(os.getcwd() + '/sounds/ff_alarm.wav')


httpd = HTTPServer(('127.0.0.1', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()