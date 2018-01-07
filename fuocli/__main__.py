import sys
from contextlib import contextmanager
from socket import socket, AF_INET, SOCK_STREAM


SIMPLE_CMD_LIST = (
    'pause', 'resume', 'stop',
    'next', 'previous', 'list',
)


def cmd_simple(cli, cmd):
    cli.send('{}\n'.format(cmd))
    return cli.recv()


def ruok():
    return 'what? are you kidding?'


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


def cmd_resume(cli):
    if len(sys.argv) != 2:
        return ruok()
    else:
        cli.send('resume\n')
        return cli.recv()


def cmd_next(cli):
    if len(sys.argv) != 2:
        return ruok()
    else:
        cli.send('next\n')
        return cli.recv()


def cmd_add(cli):
    if len(sys.argv) not in (2, 3):
        return ruok()
    elif len(sys.argv) == 2:
        furi_list = []
        for line in sys.stdin:
            furi_list.append(line.strip())
    else:
        furi_list = [sys.argv[2]]

    cli.send('add {}\n'.format(','.join(furi_list)))
    rv = cli.recv()
    return rv


def cmd_list(cli):
    if len(sys.argv) != 2:
        return ruok
    else:
        cli.send('list\n')
        return cli.recv()


def cmd_remove(cli):
    if len(sys.argv) != 3:
        return ruok
    else:
        furi = sys.argv[2]
        cli.send('remove {}\n'.format(furi))
        return cli.recv()


def cmd_status(cli):
    if len(sys.argv) != 2:
        return ruok
    else:
        cli.send('status\n')
        return cli.recv()


def cmd_show(cli):
    if len(sys.argv) != 3:
        return ruok()
    else:
        identifier = sys.argv[2]
        cli.send('show {}\n'.format(identifier))
        return cli.recv()


def cmd_search(cli):
    if len(sys.argv) != 3:
        return ruok()
    else:
        q = sys.argv[2]
        cli.send('search {}\n'.format(q))
        return cli.recv()


def main():

    args_length = len(sys.argv)
    if args_length == 1:
        return ruok()

    cmd = sys.argv[1]
    with connect() as cli:
        cli.recv(1024)  # receive welcome message
        if cmd in SIMPLE_CMD_LIST:
            rv = cmd_simple(cli, cmd)
        elif cmd == 'play':
            rv = cmd_play(cli)
        elif cmd == 'show':
            rv = cmd_show(cli)
        elif cmd == 'add':
            rv = cmd_add(cli)
        elif cmd == 'list':
            rv = cmd_list(cli)
        elif cmd == 'status':
            rv = cmd_status(cli)
        elif cmd == 'remove':
            rv = cmd_remove(cli)
        elif cmd == 'search':
            rv = cmd_search(cli)
        else:
            rv = 'Unknown Command'
    print(rv)
