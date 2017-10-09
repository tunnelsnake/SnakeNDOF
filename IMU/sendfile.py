import os
import socket

class Sendfile():

    def __init__(self, file="/logs/rawdata.csv"):

        PORT = 8080
        HOST = '192.168.0.111'

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST,PORT))
            s.listen(1)
            conn, addr = s.accept()
        except ConnectionError:
            print("Connection Error: File not Sent.")
            exit(1)

        fileToSend = open(file, 'rb')
        while True:
            data = fileToSend.readline()
            if data:
                conn.send(data)
            else:
                break


        fileToSend.close()
        conn.sendall('')
        conn.close()
        print("File Sent Successfully.")