from multiprocessing import Process

import receivefile
import data_parser
import clear_logs
import data_plot
import euler_transform
import os
import time


def create_plot(file="logs/pointdata.csv"):
    scatter = data_plot.Data_plot(file)



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

    print("[1] - Download Raw Data")
    print("[2] - Parse, Transform, and Graph Current Data")
    print("[3] - Parse Current Data")
    print("[4] - Transform Current Data")
    print("[5] - Graph Raw Data")
    print("[6] - Graph Transformed Data")
    print("[7] - Debug Loop (Deprecated)")
    print("[8] - Exit")
    inp = input("\nData Client>")

    if inp == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Waiting for File.")
        rf = receivefile.Receivefile()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif inp == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        dp = data_parser.Data_parser()
        print("Data Parsed.")
        x = input("X Rotation (Degrees): ")
        y = input("Y Rotation (Degrees): ")
        z = input("Z Rotation (Degrees): ")
        euler = euler_transform.Euler_transform(x, y, z)
        print("Data Transformed.")
        time.sleep(2)
        plot = data_plot.Data_plot("logs/matrixdata.csv")

    elif inp == '3':
        dp = data_parser.Data_parser()
        print("Data Parsed.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif inp == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        x = input("X Rotation (Degrees): ")
        y = input("Y Rotation (Degrees): ")
        z = input("Z Rotation (Degrees): ")
        dp = data_parser.Data_parser()
        euler = euler_transform.Euler_transform(x, y ,z)
        print("Data Transformed.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif inp == '5':
        create_plot()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


    elif inp == '6':
        create_plot("logs/matrixdata.csv")
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(2)

    elif inp == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        debugloop()

    elif inp == '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    elif inp == '':
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("Invalid Choice")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


