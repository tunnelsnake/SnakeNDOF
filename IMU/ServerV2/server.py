import socket
import time

from multiprocessing import Process
from Adafruit_BNO055 import BNO055


class Server():

    logfile = "logs/rawdata.csv"

    host = "192.168.0.104"
    port = "8080"

    active_connection = False
    collect_data = False
    collection_time = 0 #in seconds
    kill_proc = False

    def startlistener(self, bno):

            print("Awaiting Connection.")

            # socket stuff...
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(1)

            conn, addr = s.accept()
            self.active_connection = True
            sys, gyro, accel, mag = bno.get_calibration_status()

            # send all four calibrations right in a row
            conn.send(sys + gyro + accel + mag)

            data = conn.recv(1024)

            if data == '0':
                print("Sensors Uncalibrated!")
                s.close()
                self.kill_proc = True

            elif 0 < int(data) < 30:
                print("Collecting " + data + " Seconds of Data.")
                self.collection_time = int(data)
                self.collect_data = True

                #stall until file is written - signified by reset in collect_data
                time.sleep(int(self.collection_time))
                while True:
                    if(self.collect_data == False):
                        time.sleep(3)
                        break

                #now send the physical file
                try:
                    f = open(self.inputfile, 'rb')
                except IOError:
                    print("An Error Occurred Reading the File.")
                    exit(1)

                while True:
                    data = f.readline()
                    if data:
                        conn.send(data)
                    else:
                        break

                f.close()
                s.close()
                conn.close()

            else:
                print("Unexpected Data!")
                s.close()
                self.kill_proc = True



    def __init__(self):


        # Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
        bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)

        # Clear the terminal initially.

        # Initialize the BNO055 and stop if something went wrong.
        if not bno.begin():
            raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

        try:
            f = open(self.logfile, "a")
        except IOError:
            print("Error Opening File for Writing")

        print("\n")
        input("Press a Key to Begin Calibration...\n")


        print("Starting Calibration.")
        print("Place Sensor on Table for Gyroscope Calibration.")

        # Gyroscope Calibration
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if gyro == 3:
                break
            else:
                time.sleep(.25)

        # Magnetometer Calibration
        print("Gyroscope Calibration Complete.\nBeginning Magnetometer Calibration. ")
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if mag == 3:
                break
            else:
                time.sleep(.25)

        # Accelerometer Calibration
        print("Magnetometer Calibration Complete.\nBeginning Accelerometer Calibration.")
        print("Move Sensor at 45 Degree Angles")
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if accel == 3:
                break
            else:
                time.sleep(.25)

        print("Calibrations Complete.\nAwaiting System Confirmation.")
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if sys == 3:
                break
            else:
                time.sleep(.25)

        while True:
            p = Process(target=self.startlistener, args=(bno,))

            while True:
                if(self.active_connection):

                    while True:

                        if(self.kill_proc == True):
                            p.terminate()
                            self.collection_time = 0
                            self.kill_proc = False
                            self.collect_data = False
                            self.active_connection = False

                        elif self.collect_data == True and self.collection_time > 0:

                            start_time = time.time() * 1000 #milliseconds
                            f = open(self.logfile, "w") #file object

                            while True:

                                # Read the Euler angles for heading, roll, pitch (all in degrees).
                                heading, roll, pitch = bno.read_euler()
                                # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
                                sys, gyro, accel, mag = bno.get_calibration_status()

                                # Read linear Acceleration data
                                # accel_x,accel_y,accel_z = bno.read_linear_acceleration()

                                # Read full acceleration data (with gravity)
                                accel_x, accel_y, accel_z = bno.read_linear_acceleration()

                                # Append data to CSV file
                                t = time.asctime()
                                t = (time.time() * 1000) - start_time
                                f.write(str(t) + "," + str(heading) + "," + str(roll) + "," + str(pitch) + "," + str(
                                    accel_x) + "," + str(accel_y) + "," + str(accel_z) + "," + str(sys) + "," + str(
                                    gyro) + "," + str(accel) + "," + str(mag) + "\n")
                                if (((time.time() * 1000) - start_time) >= float(self.collection_time) * 1000):
                                    break

                                #down and dirty way to give the other thread time to do its thing.
                                self.collect_data = False

                                time.sleep(5)
                                p.terminate()

                                self.kill_proc = False
                                self.collection_time = 0
                                self.active_connection = False


                        else:
                            p.terminate()
                            self.collection_time = 0
                            self.kill_proc = False
                            self.collect_data = False
                            self.active_connection = False
                else:
                    time.sleep(1)




s = Server()
