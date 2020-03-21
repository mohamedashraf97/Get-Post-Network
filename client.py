from socket import *
import os
import shutil
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input your command:")
clientSocket.send(sentence.encode())
print("-------------------", sentence.split(" ")[0])
if sentence.split(" ")[0]=="post":
    found = False
    for r, d, f in os.walk(rb"C:\\Users\\Mss.A.RAMZY\networks\\client\\"):
        for file in f:
            if sentence[1] in file:
                # print("200 OK\n", os.path.join(r, file))
               # clientSocket.send("200 OK\n".encode())
                f1 = open("C:\\Users\\Mss.A.RAMZY\networks\\client\\" + sentence.split(" ")[1], "rb")
                clientSocket.send(f1.read().encode())


                found = True

    if found == False:
        clientSocket.send("404 NOT FOUND\n".encode())

modifiedSentence = clientSocket.recv(1024)
receivedMsg = modifiedSentence.decode()
if receivedMsg == "200 OK\n":
    modifiedSentence = clientSocket.recv(1024)
    print("From Server: ", modifiedSentence.decode())
    print("C:\\Users\\Mss.A.RAMZY\networks\\client\\"+sentence.split(" ")[1])
    f = open("C:\\Users\\Mss.A.RAMZY\networks\\client\\"+sentence.split(" ")[1], "wb")
    f.write(modifiedSentence.decode())
    f.close()
else:
    print("From Server: ", receivedMsg)


clientSocket.close()