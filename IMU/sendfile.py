import socket

class Sendfile():

    def __init__(self, inputfile="logs/rawdata.csv"):

        port = 8080
        host = '192.168.0.104'

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host,port))
            s.listen(1)
            conn, addr = s.accept()
        except ConnectionError:
            print("Connection Error: File not Sent.")
            exit(1)

        try:
            f = open(inputfile, 'rb')
        except IOError:
            print("An Error Occurred Reading the File.")
        while True:
            data = f.readline()
            if data:
                conn.send(data)
            else:
                break

        f.close()
        s.close()
        conn.close()
        print("File Sent To " + host + " Successfully.")

