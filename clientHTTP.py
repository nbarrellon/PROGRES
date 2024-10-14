from socket import *
import time

serverName = "127.0.0.1"
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send('GET clientTCP.py'.encode('utf-8'))
print("Reponse du serveur:\n",clientSocket.recv(2048).decode('utf-8'))
    
clientSocket.close()
                                            