# Creating the socket
import signal
import socket
import sys
import select
import os

not_stopped = False
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = int(sys.argv[1])  # Port to listen on (non-privileged ports are > 1023)
if PORT < 1 or PORT > 65535:
    sys.stderr.write('ERROR: ')
    exit(-1)

signal.signal(signal.SIGTERM, signal.SIG_DFL)
# signal.signal(signal.TERM, handler)
# signal.signal(signal.INT, signal.SIG_DFL)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(10)

    print('Waiting for incoming connections on', sock)

    ready = select.select([sock], [], [], 100)
    while ready[0]:

        conn, addr = sock.accept()
        conn.settimeout(10.1)
        print('Connected by', addr)
        try:
            conn.send(b'accio\r\n')
#tesy
        except:
            print("Couldn't send accio")
        try:
            data = conn.recv(2048)
            bytes_recv = sys.getsizeof(data)
            print(bytes_recv)
        except socket.timeout:
            sys.stderr.write('ERROR: aborting connection\n')


        data = None
        try:
            conn.close()
            print('connection closed')
        except:
            print("Conn not open")

sock.close()

