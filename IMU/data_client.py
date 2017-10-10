from multiprocessing import Process

import receivefile
import data_parser
import clear_logs
import data_plot
import os
import time


def create_plot():
    scatter = data_plot.Data_plot()


def debugloop():

    proc_spawned = False

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Waiting for File.")

        # sleep for a second, because on repeat the logs will clear too fast for the new plot
        time.sleep(1)

        c = clear_logs.Clear_logs(False)
        rf = receivefile.Receivefile()

        if proc_spawned: p.terminate()
        dp = data_parser.Data_parser()

        p = Process(target=create_plot, args='')
        p.start()
        proc_spawned = True



while True:
    print("[1] - Start Debug Loop")
    print("[2] - Download rawdata.csv")
    print("[3] - Graph Current Data")
    print("[4] - Exit")
    inp = input("Default : [1]\nData Client>")

    if inp == '1' or inp == '':
        debugloop()

    elif inp == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Waiting for File.")
        rf = receivefile.Receivefile()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif inp == '3':
        create_plot()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif inp == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    else:
        print("Invalid Choice")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


