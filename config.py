import datetime

PORT = 8091
HOST = "127.0.0.1"


class StatusCodes:
    OK = 200
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405


HEADERS = {'Date': datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z'), 'Server': 'MyHTTPServer',
           'Content-Length': 0, 'Content-Type': 'text/html', 'Connection': 'close'}
