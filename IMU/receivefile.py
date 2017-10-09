import os
import socket

class Receivefile():

    def __init__(self, outputpath='/logs/rawdata.csv'):

        PORT = 8080
        HOST = "192.168.0.104"

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
        except ConnectionError:
            print("Connection Failed.")
            exit(1)

        f = open(outputpath, "wb")
        while True:
            data = socket.recv(1024)
            if  data:
                f.write(data)
            else:
                f.close()
                break
        socket.close()
        print("File Received")
        exit(0)