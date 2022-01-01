# from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World this is Python HTTP Server!'.encode())


def main():
    PORT = 8080
    server = HTTPServer(('', PORT), Handler)
    print('Server Running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()