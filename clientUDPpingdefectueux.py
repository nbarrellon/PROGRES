from socket import *
from time import perf_counter
serverName = "127.0.0.1"
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_DGRAM)
RTT = []
delay = 0.1
for i in range(4):
    t0 = perf_counter()
    message = ("ping n°"+str(i)).encode('utf-8')
    clientSocket.sendto(message,(serverName,serverPort))
    clientSocket.settimeout(delay)
    try:
        modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
        t1 = perf_counter()
        reponse = modifiedMessage.decode('utf-8')
        RTT.append((reponse,(t1-t0)*1000))
    except timeout:
        print("Le message s'est perdu !")
somme = 0
nbping = 0
for pong in RTT:
    print("pong : ",pong[0],"reçu en ",pong[1],"ms")
    somme += pong[1]
    nbping += 1
print("RTT moyen = ",somme/nbping,"ms")
clientSocket.close()