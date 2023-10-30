import os
import mimetypes
from urllib import request, parse

from config import StatusCodes, HEADERS
from parse_args import DOCUMENT_ROOT


class RequestHandler:
    def __init__(self, data):
        self.client_data = data.split('\r\n')
        self.user_headers = {}

    def check_query_params(self):
        list_user_request = self.user_headers['Request'].split('/')
        if '?' in list_user_request[-1]:
            list_user_request[-1] = list_user_request[-1][:
                                                          list_user_request[-1].index('?')]
        return '/'.join(list_user_request)

    def parse_data(self):
        method, request, protocol = self.client_data[0].split(' ')
        self.user_headers['Method'] = method
        self.user_headers['Request'] = parse.unquote(request)
        self.user_headers['Protocol'] = protocol
        if self.user_headers['Request'].endswith('/'):
            self.user_headers['Request'] += 'index.html'
        self.user_headers['Request'] = self.check_query_params()

    def create_headers(self, code, path=None):
        if code == StatusCodes.OK:
            HEADERS['Content-Length'] = os.path.getsize(path)
            HEADERS['Content-Type'] = mimetypes.guess_type(
                request.pathname2url(path))[0]
            join_headers = '\r\n'.join(
                [f'{x[0]}: {x[1]}' for x in HEADERS.items()])
            HDRS = f'HTTP/1.1 {StatusCodes.OK} OK\r\n{join_headers}\r\n\r\n'
            return HDRS
        elif code == StatusCodes.FORBIDDEN:
            HEADERS['Content-Length'] = os.path.getsize(path)
            HEADERS['Content-Type'] = mimetypes.guess_type(
                request.pathname2url(path))[0]
            join_headers = '\r\n'.join(
                [f'{x[0]}: {x[1]}' for x in HEADERS.items()])
            HDRS = f'HTTP/1.1 {StatusCodes.FORBIDDEN} FORBIDDEN\r\n{join_headers}\r\n\r\n'
            return HDRS
        elif code == StatusCodes.NOT_FOUND:
            join_headers = '\r\n'.join([f'{x[0]}: {x[1]}' for x in HEADERS.items(
            ) if x[0] not in ('Content-Type', 'Content-Length')])
            HDRS = f'HTTP/1.1 {StatusCodes.NOT_FOUND} NOT FOUND\r\n{join_headers}\r\n\r\n'
            return HDRS
        else:
            join_headers = '\r\n'.join([f'{x[0]}: {x[1]}' for x in HEADERS.items(
            ) if x[0] not in ('Content-Type', 'Content-Length')])
            HDRS = f'HTTP/1.1 {StatusCodes.METHOD_NOT_ALLOWED} ERROR\r\n{join_headers}\r\n\r\n'
            return HDRS

    def find_attachment(self):
        with open(DOCUMENT_ROOT + self.user_headers['Request'], 'rb') as file:
            response = file.read()
        return response

    def send_response(self):
        try:
            self.parse_data()
        except ValueError:
            HDRS = self.create_headers(code=StatusCodes.METHOD_NOT_ALLOWED)
            return HDRS.encode('utf-8')
        if self.user_headers['Method'] == 'GET':
            try:
                HDRS = self.create_headers(
                    code=StatusCodes.OK, path=DOCUMENT_ROOT + self.user_headers['Request'])
            except FileNotFoundError:
                HDRS = self.create_headers(code=StatusCodes.NOT_FOUND)
                return HDRS.encode('utf-8')
            content = self.find_attachment()
            return HDRS.encode('utf-8') + content
        elif self.user_headers['Method'] == 'HEAD':
            try:
                HDRS = self.create_headers(
                    code=StatusCodes.OK, path=DOCUMENT_ROOT + self.user_headers['Request'])
            except FileNotFoundError:
                HDRS = self.create_headers(code=StatusCodes.NOT_FOUND)
                return HDRS.encode('utf-8')
            return HDRS.encode('utf-8')
        elif self.user_headers['Method'] not in ('GET', 'HEAD'):
            HDRS = self.create_headers(code=StatusCodes.METHOD_NOT_ALLOWED)
            return HDRS.encode('utf-8')
