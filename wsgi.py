import os
from paste.deploy import loadapp
from wsgiref.simple_server import make_server

application = loadapp('config:' + os.path.dirname(__file__) + '/configurations/test.ini')

def serve(port=8099):
    httpd = make_server('', port, application)
    httpd.serve_forever()

if __name__ == "__main__":
    serve()
