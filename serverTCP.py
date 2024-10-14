from socket import *
import datetime
import time
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen()
print("Server Ready")
while True:
    connectionSocket,address = serverSocket.accept()
    print("Socket entrant :<",address[0],",",address[1],">")
    heure = str(datetime.datetime.now())
    print("L'heure du serveur est:",heure)
    message = connectionSocket.recv(2048).decode('utf-8')
    modifiedMessage = message.upper().encode('utf-8')
    connectionSocket.send(str(time.time()).encode('utf-8'))
    connectionSocket.close()