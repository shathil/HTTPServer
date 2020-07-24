# mohoque

from tcpserver import TCPServer


if __name__ == "__main__":

    serverAddr = '127.0.0.1'
    port = 8080
    d = TCPServer(serverAddr, port)
    d.start_server()

