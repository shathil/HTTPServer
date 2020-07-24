# mohoque
# TCP server base for the exchanging HTTP messages
import socket
import threading
import fcntl
import os
import errno
from time import sleep
from datetime import datetime
from HttpTests import HTTPTest


def data_exchange(cli_sock, addr):
    connected = True
    new_sock = cli_sock  # socket.socket(cli_sock)
    fcntl.fcntl(new_sock, fcntl.F_SETFL, os.O_NONBLOCK)
    print(f"{datetime.now()}: Connection from client {addr} ")
    while connected:
        try:
            request = cli_sock.recv(1024).decode('utf-8').lower()
        except socket.error as e:
            errr = e.args[0]
            if errr == errno.EAGAIN or errr == errno.EWOULDBLOCK:
                sleep(1)
                continue
            else:
                break
        else:
            if len(request) is 0:
                break

            print(f"{datetime.now()}: request {request} ")
            lines = request.split("\r\n")
            req_uri = lines[0]
            response = HTTPTest(req_uri)
            code = response.get_response_code()
            message = response.get_response(code)
            print(f"{datetime.now()}: Response: {message}")
            new_sock.sendall(message.encode('utf-8'))
    new_sock.close()


class TCPServer:

    def __init__(self, addr, port):
        # initializing the socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.addr = (addr, port)
        self.clients = 0
        try:
            self.server.bind(self.addr)
        except socket.error as e:
            print(f"{datetime.now()}: socket bind error ", e.args[0])
            return

    def start_server(self):
        server_status = False
        try:
            self.server.listen(10)
            server_status = True
        except socket.error as e:
            print(f"{datetime.now()}: socket listening error ", e.args[0])
            return

        while server_status:
            cli_sock, addr = self.server.accept()
            cli_thread = threading.Thread(target=data_exchange, args=(cli_sock, addr))
            cli_thread.start()
            self.clients = threading.active_count()
            print(f"{datetime.now()}: active clients  ", self.clients)

    def get_active_clients(self):
        return self.clients


