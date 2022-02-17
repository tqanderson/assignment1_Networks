# Reference: https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/

import socket
from _thread import *
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 53237
ThreadCount = 0

ServerSideSocket.bind((host, port))

print('Socket is on')
ServerSideSocket.listen(5)

def multi_threaded(connection):
    connection.send(str.encode('Server is on:'))
    while True:
        data = connection.recv(2048)
        response = 'Request: ' + data.decode('utf-8')
        if not data:
            break
        print(response)
        filename = data.split()[1]
        try:
            f = open(filename[1:])
            print("200 OK")
        except IOError:
            print("404 Not Found")
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded, (Client, ))
    ThreadCount += 1
    print('Thread #' + str(ThreadCount))
ServerSideSocket.close()
