import re
import sys
from socket import socket, AF_INET, SOCK_STREAM


song_identifier_re = re.compile(r'fuo://\w+:song:\d+')


def ruok():
    print('what? are you kidding')


def play():
    pass


def send(cmd):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 23333))
    sock.recv(1024)  # 接受 server welcome 消息
    sock.send(bytes(cmd, 'utf-8'))
    data = sock.recv(4096*2*2*2)
    data = data.decode()
    data = data[:-4]
    sock.close()
    return data


def cmd_play():
    if len(sys.argv) > 3:
        ruok()
    elif len(sys.argv) <= 2:
        for line in sys.stdin:
            if not line:
                continue
            if song_identifier_re.match(line):
                send('add {}'.format(line))
            else:
                print('invalid song identifier: {}'.format(line))


def cmd_show(*args, **kwargs):
    pass


def main():

    args_length = len(sys.argv)
    if args_length == 1:
        ruok()
        return

    cmd = sys.argv[1]
    if cmd == 'play':
        cmd_play()
    elif cmd == 'show':
        cmd_show(sys.argv[2:])
