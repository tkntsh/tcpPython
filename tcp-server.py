# tcp-server.py

from socket import *
# create the socket
# AF_INET == ipv4
# AF_INET6 == ipv6
# SOCK_STREAM == TCP
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
#bind a socket to some port on the server
serverSocket.bind(("",serverPort))
serverSocket.listen(5)
print ("The server is ready to receive")
while True:
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024).decode()
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence.encode())
     connectionSocket.close()

