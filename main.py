from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        x = self.wfile.write
        qs = {}
        path = self.path
        if '?' in path:
            path, tmp = path.split('?', 1)
            qs = parse_qs(tmp)

        line_auth = 'http://{}/main?TECH_SENS_COUNT'.format(qs['ip_addr'][0])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        x(b'Ok\n')
        print(line_auth)


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
