import sys
from contextlib import contextmanager
from socket import socket, AF_INET, SOCK_STREAM


def ruok():
    return 'what? are you kidding?'


def play():
    pass


class Client(object):
    def __init__(self, sock):
        self.sock = sock

    def send(self, cmd):
        return self.sock.send(bytes(cmd, 'utf-8'))

    def recv(self, num=1024*10*2):
        return self.sock.recv(num).decode('utf-8')

    def close(self):
        self.sock.close()


@contextmanager
def connect():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 23333))
    client = Client(sock)
    try:
        yield client
    except RuntimeError as e:
        print(e)
    client.close()


def cmd_play(cli):
    if len(sys.argv) != 3:
        return ruok()
    else:
        cli.send('play {}\n'.format(sys.argv[2].strip()))
        return cli.recv()


def cmd_add(cli):
    if len(sys.argv) != 2:
        return ruok()
    else:
        rv = ''
        for line in sys.stdin:
            cli.send('add {}\n'.format(line.strip()))
            rv += cli.recv()
        return rv


def cmd_show(cli):
    if len(sys.argv) != 3:
        return ruok()
    else:
        identifier = sys.argv[2]
        cli.send('show {}\n'.format(identifier))
        return cli.recv()


def main():

    args_length = len(sys.argv)
    if args_length == 1:
        return ruok()

    cmd = sys.argv[1]
    with connect() as cli:
        cli.recv(1024)  # receive welcome message
        if cmd == 'play':
            rv = cmd_play(cli)
        elif cmd == 'show':
            rv = cmd_show(cli)
        elif cmd == 'add':
            rv = cmd_add(cli)
        else:
            rv = 'Unknown Command'
    print(rv)
