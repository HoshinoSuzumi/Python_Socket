# coding: utf-8
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        CLIENT_ADDR = self.client_address[0]
        CLIENT_PORT = self.client_address[1]
        print('Client connected[%s:%s]' % (CLIENT_ADDR, CLIENT_PORT))
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    break
                print('->%s:' % CLIENT_PORT, data)
            except ConnectionResetError:
                break
        self.request.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), MyTCPHandler)
    server.serve_forever()  # 链接循环
