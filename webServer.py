from http.server import HTTPServer, BaseHTTPRequestHandler
from pydub import AudioSegment
from pydub.playback import play

ip_whitelist = [
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
        
        song = AudioSegment.from_mp3("ff_alarm.mp3")
        play(song)


httpd = HTTPServer(('172.29.28.181', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
