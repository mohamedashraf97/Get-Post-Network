# import socket
# from SocketServer import ThreadingMixIn

from socket import *
import os
import shutil
from threading import Thread

class ClientThread(Thread):
    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.connectionSocket = conn
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        # while True:
        # data = conn.recv(2048)

        sentence = self.connectionSocket.recv(1024).decode()
        print(sentence)
        arr = sentence.split()
        if arr[0] == "get":
            found = False
            for r, d, f in os.walk(r"C:\Users\Mss.A.RAMZY\networks\server"):
                for file in f:
                    if arr[1] in file:
                        # print("200 OK\n", os.path.join(r, file))
                        self.connectionSocket.send("200 OK\n".encode())
                        f2 = open("C:\Users\Mss.A.RAMZY\networks\server" + arr[1], "r")
                        f1 = open("C:\Users\Mss.A.RAMZY\networks\server" + arr[1], "r")
                        self.connectionSocket.send(f1.read().encode())

                        found = True

            if found == False:
                self.connectionSocket.send("404 NOT FOUND\n".encode())

        if arr[0] == "post":
            f = open("C:\Users\Mss.A.RAMZY\networks\server" + arr[1], "w")
            Recievedsentence = self.connectionSocket.recv(1024)
            f.write(Recievedsentence.decode())
            f.close()

            self.connectionSocket.close()



# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 12000
BUFFER_SIZE = 1024

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print
    "Multithreaded Python server : Waiting for connections from TCP clients..."
    (connection, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port, connection)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()

