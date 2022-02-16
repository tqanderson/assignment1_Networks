from socket import *
import datetime
import time
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket

serverPort = 53235
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)  # network buffer
        filename = message.split()[1]
        f = open(filename)
        outputdata = f.read()
        now = datetime.datetime.now()
        # Send one HTTP header line into socket
        print(outputdata)
        # Send the content of the requested file to the client
        http_header = "HTTP/1.1 200 OK"

        basic_header = {
            "Date": now.strftime("%Y-%m-%d %H:%M"),
            "Content-Length": len(outputdata),
            "Connection": "Keep Alive",
            "Content Type": "text/html"
        }

        following_header = "\r\n".join("%s:%s" % (item, basic_header[item]) for item in basic_header)
        print
        "following_header:", following_header
        connectionSocket.send("%s\r\n%s\r\n\r\n" % (http_header, following_header))

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
# Send response message for file not found
        connectionSocket.close()
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
