import cgi
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import PyTess


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        try:
            if self.path.endswith(".html"):
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query = cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)

            self.end_headers()
            upfilepath = query.get('upfile')
            dfilepath = query.get('dfile')

            w = open(dfilepath[0], 'w')

            Image = PyTess.ImageRead(upfilepath[0])
            ImageData = Image.ImgRead()
            w.write(ImageData)
            w.close()

            self.wfile.write("<HTML>POST OK.<BR><BR>")
        except:
            pass


def main():
    try:
        server = HTTPServer(('localhost', 9000), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
