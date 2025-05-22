from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, DevOps World!")

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port ' + str(port) + '...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
