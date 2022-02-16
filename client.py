from socket import *
import sys

server_host = # NEED TO FIND HOST NAME
server_port = 53235
filename = input("Please enter the filename you are looking for (i.e HelloWorld.html)")

h_port = "%s:%s" %(server_host, server_port)

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, int(server_port)))
    header = {
        "first_header": "GET /%s HTTP/1.1" % (filename),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": h_port,
    }
    http_header = "\r\n".join("%s:%s" % (item, header[item]) for item in header)
    print (http_header)
    client_socket.send("%s\r\n\r\n" % (http_header))

except IOError:
    sys.exit(1)
final = ""
response_message = client_socket.recv(1024)
while response_message:
    final += response_message
    response_message = client_socket.recv(1024)

client_socket.close()
print("final:", final)

