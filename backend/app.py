from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import json

colors = ["red","blue","green","yellow","purple","orange"]

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        color = random.choice(colors)

        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()

        response = {"color": color}
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0",5000), handler)

print("Backend running on port 5000")
server.serve_forever()
