import sys
from socket import socket, AF_INET, SOCK_STREAM


def send(cmd):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 23333))
    sock.recv(1024)  # 接受 server welcome 消息
    sock.send(bytes(cmd, 'utf-8'))
    data = sock.recv(4096)
    data = data.decode()
    if data.endswith('OK\n'):
        data = data[:-4]
        sock.close()
        return data
    print('出现异常.')


def main():
    cmd = sys.argv[1]
    content = send(cmd)
    print(content)
