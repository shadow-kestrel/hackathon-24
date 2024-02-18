# TODO import sentiment analysis, keyword extraction

import socketserver
import subprocess
import os
from http.server import BaseHTTPRequestHandler


class MessageHandler(BaseHTTPRequestHandler):
    """
    Handler class for the server.

    Takes a message in a HTTP POST from the frontend, passes it into the ML
    bits, passes their outputs into the gif generator. It then puts this gif
    into imgcache and responds to the request with the URL of the gif.
    """

    def do_GET(self):
        message = self.rfile.readline()

        # pass message to ML bits TODO populate the following vars
        sentiment = 1
        caption = u"Sticking your gyatt out for the rizzler \U0001F9F0"

        # note to future self: at some point probably set up the script to
        # periodically clear out old gifs
        out_file_name = "out0000000.gif"
        out_file_path = "/var/www/html/catbot/imgcache/" + out_file_name

        # subprocess.run((
        #     "magick",
        #     "[the args to make magick CLI caption the gif]"
        # ))

        if os.path.exists(out_file_path):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"http://kestrel.gay/catbot/imgcache/" +
                             out_file_name)
        else:
            self.send_response(500)
            self.end_headers()

class SocketHttpServer(socketserver.ThreadingUnixStreamServer):
    def get_request(self):
        request, client_address = super(SocketHttpServer, self).get_request()
        return request, ("local", 0)

if __name__ == "__main__":
    server = SocketHttpServer(("/tmp/catbot.socket"), MessageHandler)
    server.serve_forever()
