__author__ = "Jacob Thomas"

import euler_transform as euler

#This file takes the output of data_aq.py and spits out point data to another csv file

class Data_parser():

    def __init__(self, verbose=False, inputfile="logs/rawdata.csv", outputfile="logs/pointdata.csv"):

        try:
            readfile = open(inputfile, "r")
        except IOError:
            print("An Error Occurred Opening " + inputfile + " for Reading")

        try:
            writefile = open(outputfile, "w").close() #clear out the Point Data file
        except IOError:
            print("An Error Occurred Opening " + outputfile + " for Clearing")

        try:
            writefile = open(outputfile, "a")
        except:
            print("An Error Occurred Opening " + outputfile + " for Writing")

        line = self.parseline(readfile.readline())

        if(line == ''):
            print("Data File is Empty!")
            exit(1)

        # This is setting the first set of values that will determine the first reference point

        s_time = float(line[0])
        s_yaw = float(line[1])
        s_roll = float(line[2])
        s_pitch = float(line[3])
        s_accelx = float(line[4])
        s_accely = float(line[5])
        s_accelz = float(line[6])

        ref_x = 0
        ref_y = 0
        ref_z = 0

        # The rotations in degrees
        rotation_x = 30
        rotation_y = 0
        rotation_z = 0

        while True:
            line = self.parseline(readfile.readline())


            if line[0] == '':
                break

            dx = 0
            dy = 0
            dz = 0

            d_time = float(line[0])
            d_yaw = float(line[1])
            d_roll = float(line[2])
            d_pitch = float(line[3])
            d_accelx = float(line[4])
            d_accely = float(line[5])
            d_accelz = float(line[6])

            timedifference = (d_time - s_time) / 1000 #put it in seconds

            #vf = vi + at but vi is zero because I don't really know what it is...
            vf_x = s_accelx * timedifference
            vf_y = s_accely * timedifference
            vf_z = s_accelz * timedifference

            if verbose: print("x velocity: " + str(vf_x) + " y velocity: " + str(vf_y) + " z velocity: " + str(vf_z) + "\n")

            #d = vi * t + .5a * t^2 but vi is again 0 so basically .5a * t^2
            dx = (.5 * vf_x * (timedifference * timedifference)) + ref_x
            dy = (.5 * vf_y * (timedifference * timedifference)) + ref_y
            dz = (.5 * vf_z * (timedifference*timedifference)) + ref_z

            #dx, dy, dz = euler.Euler_transform().apply_matrix(dx, dy, dz, 0, 0, 0)

            if verbose: print("x distance: " + str(dx) + " y distance: " + str(dy) + " z distance: " + str(dz) + "\n")

            #Write points to another CSV file

            writefile.write(str(dx) + "," + str(dy) + "," + str(dz) + "\n")

            #WRITE PURE ACCELERATION DATA
            #writefile.write(str(s_accelx) + "," + str(s_accely) + "," + str(s_accelz) + "\n")


            # update recursive values for the next iteration

            ref_x = dx
            ref_y = dy
            ref_z = dz

            s_time = d_time
            s_yaw = d_yaw
            s_roll = d_roll
            s_pitch = d_pitch
            s_accelx = d_accelx
            s_accely = d_accely
            s_accelz = d_accelz

    def parseline(self, line):
        line = line.replace("\n", "")
        retlist = line.split(",")
        return retlist
