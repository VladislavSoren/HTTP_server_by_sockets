import socket

from multiprocessing import Process

from config import PORT, HOST
from handlers import RequestHandler
from parse_args import WORKERS


class MyHTTPServer:
    def __init__(self, host=HOST, port=PORT):
        self.hostname = host
        self.port = port
        self.mysocket = self.init_socket()

    def init_socket(self):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # mysocket.settimeout(10)
        mysocket.bind((self.hostname, self.port))
        mysocket.listen(10)
        return mysocket

    def server_runner(self):
        while True:
            client_socket, address = self.mysocket.accept()
            data = client_socket.recv(1024).decode('utf-8')
            request_handler = RequestHandler(data)
            client_socket.send(request_handler.send_response())
            client_socket.shutdown(socket.SHUT_WR)
            client_socket.close()


if __name__ == '__main__':
    server = MyHTTPServer()
    process_list = []
    for i in range(WORKERS):
        process = Process(target=server.server_runner)
        process.daemon = True
        process.start()
        process_list.append(process)
    try:
        for process in process_list:
            process.join()
    except KeyboardInterrupt:
        for proc in process_list:
            if proc.is_alive():
                server.mysocket.close()
