from socket import *
from random import randint
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("server ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message reçu")
    if randint(0,1):
        modifiedMessage = message.decode('utf-8').upper()
        serverSocket.sendto(modifiedMessage.encode('utf-8'),clientAddress)
        print("Réponse envoyée")