from socket import *
import time

serverName = "127.0.0.1"
serverPort = 1234
for _ in range(5):
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send('GET heure Serveur'.encode('utf-8'))
    heureServeur = float(clientSocket.recv(2048).decode('utf-8'))
    heureClient = time.time()
    print("Différence de temps entre les deux horloges =",(heureClient-heureServeur)*1000,"ms")
    time.sleep(2)
clientSocket.close()
                                            