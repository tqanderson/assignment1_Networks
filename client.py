from socket import *
import sys

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = "/" + sys.argv[3]
req = "GET "+str(filename)+" HTTP/1.1"

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, int(server_port)))
    client_socket.send(req.encode())

except IOError:
    sys.exit(1)
final = ""
response_message = client_socket.recv(1024)
while response_message:
    final += response_message.decode("utf-8")
    response_message = client_socket.recv(1024)

client_socket.close()
print("final:", final)
