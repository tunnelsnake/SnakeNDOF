# Copyright (c) 2015 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# Code Adapted By Jacob Thomas. Original may be found at https://github.com/adafruit/Adafruit_Python_BNO055

import logging
import sys
import time
import os

from Adafruit_BNO055 import BNO055


class Data_aq():


    def __init__(self, file="/logs/rawdata.csv"):

        # Create and configure the BNO sensor connection.  Make sure only ONE of the
        # below 'bno = ...' lines is uncommented:
        # Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
        bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)
        # BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
        # and RST connected to pin P9_12:
        # bno = BNO055.BNO055(rst='P9_12')

        # Clear the terminal initially.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Enable verbose debug logging if -v is passed as a parameter.
        if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
            logging.basicConfig(level=logging.DEBUG)

        # Initialize the BNO055 and stop if something went wrong.
        if not bno.begin():
            raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

        # Print system status and self test result.
        status, self_test, error = bno.get_system_status()
        print('System status: {0}'.format(status))
        print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
        # Print out an error if system status is in error mode.
        if status == 0x01:
            print('System error: {0}'.format(error))
            print('See datasheet section 4.3.59 for the meaning.')

        # Print BNO055 software revision and other diagnostic data.
        sw, bl, accel, mag, gyro = bno.get_revision()
        print('Software version:   {0}'.format(sw))
        print('Bootloader version: {0}'.format(bl))
        print('Accelerometer ID:   0x{0:02X}'.format(accel))
        print('Magnetometer ID:    0x{0:02X}'.format(mag))
        print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

        try:
            f = open("rawdata.csv", "a")
        except IOError:
            print("Error Opening " + file + " for Writing")

        print("\n")
        input("Press a Key to Begin Calibration...\n")

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Starting Calibration... \n")
        print("Place Sensor on Table for Gyroscope Calibration... \n")

        # Gyroscope Calibration
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if gyro == 3:
                break
            else:
                time.sleep(.25)

        # Magnetometer Calibration
        print("Accelerometer Calibration Complete. Magnetometer Calibration Beginning... \n")
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if mag == 3:
                break
            else:
                time.sleep(.25)

        # Accelerometer Calibration
        print("Gyroscope Calibration Complete. Accelerometer Calibration Beginning... \n")
        print("Move Sensor at 45 Degree Angles\n")
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if accel == 3:
                break
            else:
                time.sleep(.25)

        print("Calibration Complete. Awaiting System Confirmation... \n")
        while True:
            sys, gyro, accel, mag = bno.get_calibration_status()
            if sys == 3:
                break
            else:
                time.sleep(.25)

        os.system('cls' if os.name == 'nt' else 'clear')

        data_time = input("How many seconds of Data Acquisition? \n")
        input("Press a Key to Begin Acquisition...")

        os.system('cls' if os.name == 'nt' else 'clear')

        print('Reading BNO055 data for ' + data_time + " Seconds...")
        start_time = time.time() * 1000
        while True:

            # Read the Euler angles for heading, roll, pitch (all in degrees).
            heading, roll, pitch = bno.read_euler()
            # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
            sys, gyro, accel, mag = bno.get_calibration_status()

            # Read linear Acceleration data
            accel_x,accel_y,accel_z = bno.read_linear_acceleration()

            #Append data to CSV file
            t = time.asctime()
            t = (time.time() * 1000) - start_time
            f.write(str(t) + "," + str(heading) + "," + str(roll) + "," + str(pitch) + "," + str(accel_x) + "," + str(accel_y) + "," + str(accel_z) + "," +  str(sys) + "," + str(gyro) + "," + str(accel) + "," + str(mag) + "\n")
            if(((time.time() * 1000) - start_time) >= float(data_time) * 1000):
                break

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Data Acquisition Completed.")
        input("Press a key to Exit...")
        exit(0)