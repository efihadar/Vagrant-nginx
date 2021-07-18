#!/usr/bin/python3

import http.server
import requests
from datetime import datetime

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        currentmonth = int(datetime.today().month)
        body = requests.get(f"https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year=now&month={currentmonth}&ss=on&mf=on&c=on&geo=geoname&geonameid=3448439&m=50&s=on").text
        body += requests.get(f"https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year=now&month={currentmonth + 1}&ss=on&mf=on&c=on&geo=geoname&geonameid=3448439&m=50&s=on").text
        body += requests.get(f"https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year=now&month={currentmonth + 2}&ss=on&mf=on&c=on&geo=geoname&geonameid=3448439&m=50&s=on").text
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode())
        self.wfile.close()

try:
    server = http.server.HTTPServer(('localhost', 8080), MyHandler)
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
    