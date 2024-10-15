from socket import *
from pathlib import Path

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM) #SOCK_STREAM => TCP
serverSocket.bind(('',serverPort))
serverSocket.listen()
print("Server Ready")
while True:
    connectionSocket,address = serverSocket.accept()
    print("Socket entrant :<",address[0],",",address[1],">")
    requete = connectionSocket.recv(2048).decode('utf-8')
    if "GET" not in requete:
        connectionSocket.send("Erreur 400 - Not GET".encode('utf-8'))
    else:
        fichier = Path(requete[4:])
        if not fichier.is_file():
            connectionSocket.send("Erreur 404 - File not found".encode('utf-8'))
        else:
            with open(fichier) as f:
                connectionSocket.send(f.read().encode('utf-8'))
                connectionSocket.close()

    