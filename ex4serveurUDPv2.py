from socket import *
from pathlib import Path

def datagramme(donnee,nb,numero):
    return str(nb)+"###"+str(numero)+"###"+donnee

serverPort = 1234
serverSocket = socket(family=AF_INET,type=SOCK_DGRAM) #DGRAM pour DATAGRAMME => UDP
serverSocket.bind(('',serverPort))
print("Server Ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message reçu de ",clientAddress[0])
    requete = message.decode('utf-8')
    #Test de la requête
    if "GET" not in requete:
        serverSocket.sendto("Erreur 400 - Not GET".encode('utf-8'),clientAddress)
        print("Erreur 400 envoyée, manque GET")
    #envoi des fichiers par paquets de 256o
    else:
        fichier = Path(requete[4:-6]) #on ote le GET de la requete ainsi que les \r\n\r\n
        print("Fichier demandé par le client :",fichier)
        if not fichier.is_file():
            serverSocket.sendto("Erreur 404 - File not found".encode('utf-8'),clientAddress)
            print("Erreur 404  envoyée - File not found")
        else:
            fichier = requete[4:-6]
            with open(fichier) as f:
                fichier_a_envoyer = f.read()
            
            liste_datagramme = [] #on coupe la donnée en morceaux de 256o
            nb_datagramme = len(fichier_a_envoyer)//256+1 #nombre de datagrammes necessaires (si MSS=256o)
            while len(fichier_a_envoyer):
                liste_datagramme.append(datagramme(fichier_a_envoyer[:256]))
                fichier_a_envoyer = fichier_a_envoyer[256:]
            #envoie du dernier datagramme incomplet
            for numero_datagramme in range(len(liste_datagramme)):
                print("Envoi datagramme ",numero_datagramme)
                serverSocket.sendto(datagramme(fichier_a_envoyer[:256],nb_datagramme,numero_datagramme).encode('utf-8'),clientAddress)
            
    #Pour mettre fin au flux
    print("Envoi réalisé") 
    serverSocket.sendto("ENVOI TERMINE".encode('utf-8'),clientAddress)
            