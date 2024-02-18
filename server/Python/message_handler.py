# TODO import sentiment analysis, keyword extraction

import socketserver
from http.server import BaseHTTPRequestHandler


class MessageHandler(BaseHTTPRequestHandler):
    """
    Handler class for the server.

    Takes a message in a HTTP POST from the frontend, passes it into the ML
    bits, passes their outputs into the gif generator. It then puts this gif
    into imgcache and responds to the request with the URL of the gif.
    """

    def handle(self):
        self.data = self.rfile.read()

        # TODO
