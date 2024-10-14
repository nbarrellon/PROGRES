from socket import *
from pathlib import Path

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM) #DGRAM pour DATAGRAMME => UDP
serverSocket.bind(('',serverPort))
serverSocket.listen()
print("Server Ready")
while True:
    connectionSocket,address = serverSocket.accept()
    print("Socket entrant :<",address[0],",",address[1],">")
    requete = connectionSocket.recv(2048).decode('utf-8')
    #Test de la requête
    if "GET" not in requete:
        connectionSocket.send("Erreur 400 - Not GET".encode('utf-8'))
    #envoi des fichiers par paquets de 256o
    else:
        fichier = Path(requete[4:-8]) #on ote le GET de la requete ainsi que les \r\n\r\n
        if not fichier.is_file():
            connectionSocket.send("Erreur 404 - File not found".encode('utf-8'))
        else:
            with open(fichier) as f:
                fichier_a_envoyer = f.read().encode('utf-8')
            
            while len(fichier_a_envoyer)>256:
                datagramme = fichier[:256]
                fichier_a_envoyer = fichier_a_envoyer[256:]
                connectionSocket.send(datagramme)
            connectionSocket.close()