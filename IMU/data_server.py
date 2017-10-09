import data_aq
import sendfile
import clear_logs
import time
import os


os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("[1] - The Whole Shebang")
    print("[2] - Send rawdata.csv")
    print("[3] - Clear the Logs")
    print("[4] - Exit")
    inp = input("\nDefault : [0] \n Data Server>")

    if inp == '1':
        c = clear_logs.Clear_logs()
        d = data_aq.Data_aq()
        s = sendfile.Sendfile()

    elif inp == '2':
        s = sendfile.Sendfile()

    elif inp == '3':
        c = clear_logs.Clear_logs()

    elif inp == '4':
        exit(0)

    elif inp == '':
        c = clear_logs.Clear_logs()
        d = data_aq.Data_aq()
        s = sendfile.Sendfile()

    else:
        print("Invalid Option")
        time.sleep(2)


