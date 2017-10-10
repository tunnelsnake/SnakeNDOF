import os
import socket
import time

class Receivefile():

    def __init__(self, outputpath='logs/rawdata.csv'):

        port = 8080
        host = "192.168.0.104"

        while True:

            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                break
            except ConnectionError:
                time.sleep(2)

        f = open(outputpath, "wb")

        while True:
            data = s.recv(1024)
            if  data:
                f.write(data)

            else:
                f.close()
                break

        s.close()
        print("File Received from " + host)
