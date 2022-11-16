# Example usage:
#
# python select_server.py 3490

import select
import socket
import sys


def run_server(port):
    server_socket = socket.socket()
    server_socket.bind(('', port))
    server_socket.listen()

    socket_set = {server_socket}

    while True:
        read, _, _ = select.select(socket_set, {}, {})
        for s in read:
            
            if s is server_socket: 
                new_socket, _ = server_socket.accept()
                print(str(new_socket.getpeername()) + ": connected")
                socket_set.add(new_socket)
            else:
                message = s.recv(4096) 
                if not message:
                    print(str(s.getpeername()) + ": disconnected")
                    socket_set.remove(s)
                else:
                    print(str(s.getpeername()) + " " + str(len(message)) + " bytes: " + str(message))
#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
