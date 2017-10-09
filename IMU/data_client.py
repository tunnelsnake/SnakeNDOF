import receivefile
import data_parser
import clear_logs
import data_plot
from multiprocessing import process
import os
import time


def create_plot():
    while True:
        print("test")
        time.sleep(4)

while True:

    c = clear_logs.Clear_logs()
    os.system('cls' if os.name == 'nt' else 'clear')

    input("Press A Key To Begin Data Reception")

    rf = receivefile.Receivefile()
    dp = data_parser.Data_parser()
    p = process(Target=create_plot)
    p.start()
    p.join()
    input("Plot in Progress. Press Any Key to restart...")
    p.terminate()

