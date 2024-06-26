#!/usr/bin/env python3

# Spider Trap

### Configuration Section ###
# the lower and upper limits of how many links to put on each page
LINKS_PER_PAGE = (5, 10)
# the lower and upper limits of how long each link can be
LENGTH_OF_LINKS = (3, 20)
# the port to bind the webserver on 
PORT = 8000
# the delay between the receiving a request and serving up a webpage (in milliseconds)
DELAY = 350
# characters to compose random links from
CHAR_SPACE = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-/'
### End Configuration Section ###

import sys
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class Handler(BaseHTTPRequestHandler):
    webpages = None

    def generate_page(self, seed):
        """Generate a webpage containing only random links"""

        html = '<html>\n<head>\n<title>Welcome to the Meisterlos</title>\n</head>\n<body style="text-align:center;">\n'
        html += '<h1 style="color:#FF5733;">Welcome to the Meisterlos</h1>\n'
        html += '<p style="font-size:20px;">Discover the wonders of the Meisterlos!</p>\n'

        # Güzel bir giriş sayfası eklendi
        html += '<div style="margin-top: 50px; background-color: #f0f0f0; width: 300px; margin-left: auto; margin-right: auto; padding: 20px; border-radius: 10px;">'
        html += '<h2 style="color: #333;">Login</h2>'
        html += '<form style="text-align: left;">'
        html += '<label for="username" style="display: block; margin-bottom: 10px;">Username:</label>'
        html += '<input type="text" id="username" name="username" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px;">'
        html += '<label for="password" style="display: block; margin-bottom: 10px;">Password:</label>'
        html += '<input type="password" id="password" name="password" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px;">'
        html += '<input type="submit" value="Login" style="width: 100%; padding: 10px; margin-top: 10px; background-color: #FF5733; color: #fff; border: none; border-radius: 5px; cursor: pointer;">'
        html += '</form>'
        html += '</div>'

        random.seed(seed)
        # number of links to put on a page
        num_pages = random.randint(*LINKS_PER_PAGE)

        # check if a file was provided
        if self.webpages is None:
            # generate some random links
            for i in range(num_pages):
                address = ''.join([random.choice(CHAR_SPACE) for i in range(random.randint(*LENGTH_OF_LINKS))])
                html += '<a href="' + address + '">' + address + '</a><br>\n'
        else:
            # get links from the file contents
            for i in range(num_pages):
                address = random.choice(self.webpages)
                html += '<a href="' + address + '">' + address + '</a><br>\n'

        html += '</body>\n</html>'

        return html

    def do_HEAD(self):
        """Sends header information"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """Responds to any webpage request with a page generated by the generate_page function"""

        # sleep() takes number of seconds, but accepts floating values
        # DELAY should be in milliseconds
        time.sleep(DELAY / 1000.0)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # seed the rand function with the current URL path
        self.wfile.write(self.generate_page(self.path).encode())


def print_usage():
    print('Usage: ' + sys.argv[0] + ' [FILE]\n')
    print('FILE is file containing a list of webpage names to serve, one per line.  If no file is provided, random '
          'links will be generated.')


def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        print_usage()
        exit()

    # Use a file, if provided on command line
    if len(sys.argv) == 2:
        try:
            # read in the file
            f = open(sys.argv[1])
            Handler.webpages = f.readlines()
            f.close()

            # check for empty file
            if Handler.webpages == []:
                print('The file provided was empty.  Using randomly generated links.')
                Handler.webpages = None
        except IOError:
            print('Can\'t read input file.  Using randomly generated links.')

    try:
        print('Starting server on port %d...' % PORT)
        server = HTTPServer(('', PORT), Handler)
        print('Server started.  Use <Ctrl-C> to stop.')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Stopping server...')
        server.socket.close()
        print('Server stopped')
    except:
        print('Error starting http server on port %d.' % PORT)
        print('Make sure you are root, if needed, and that port %d is open.' % PORT)


if __name__ == '__main__':
    main()
