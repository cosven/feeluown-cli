import re
import sys
from contextlib import contextmanager
from socket import socket, AF_INET, SOCK_STREAM


song_identifier_re = re.compile(r'fuo://\w+:song:\d+')


def ruok():
    print('what? are you kidding?')


def play():
    pass


@contextmanager
def connect():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 23333))
    try:
        yield sock
    except RuntimeError as e:
        print(e)
    sock.close()


def cmd_play(sock):
    if len(sys.argv) > 3:
        ruok()
    elif len(sys.argv) <= 2:
        for line in sys.stdin:
            if not line:
                continue
            if song_identifier_re.match(line):
                sock.send(line.strip())
            else:
                print('invalid song identifier: {}'.format(line.strip()))
    else:
        sock.send('play {}'.format(sys.argv[2]))


def cmd_show(sock):
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
