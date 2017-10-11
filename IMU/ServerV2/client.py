from multiprocessing import Process

import os
import time
import socket

host = "192.168.0.104"
port = "8080"

logfile = "logs/rawdata.csv"


def requestdata(seconds):
    if 0 < int(seconds) < 30:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))

        conn, addr = s.accept()
        data = conn.recv(1024)

        if data == "3333":
            conn.send(seconds)
            f = open(logfile, "wb")

            while True:
                data = s.recv(1024)
                if data:
                    f.write(data)

                else:
                    f.close()
                    break
            print("File Received.")

        else:
            print("Must Be Between 1 and 30 Seconds!")

    else:
        print("Sensors Uncalibrated!")




while True:

    print("[1] - Start Debug Loop")
    print("[2] - Download rawdata.csv")
    print("[3] - Parse And Graph Current Data")
    print("[4] - Parse Current Data")
    print("[5] - Graph Current Data")
    print("[6] - Exit")
    inp = input("\nData Client>")



    if inp == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        seconds = input("How Many Seconds")
        requestdata(seconds)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')



    else:
        print("Invalid Choice")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


