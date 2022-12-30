from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

dat = []


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        dat.append('res')
        qs = {}
        path = self.path
        if '?' in path:
            path, tmp = path.split('?', 1)
            qs = parse_qs(tmp)
        line_auth = 'http://{}/main?TECH_SENS_COUNT'.format(qs['ip_addr'][0])
        print(line_auth)
        return 'Ok'


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
