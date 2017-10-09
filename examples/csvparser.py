import math

class Csvparser():

    def __init__(self, file):
        readfile = open(file, "r")
        writefile = open("PData.txt", "w").close() #clear out the Point Data file
        writefile = open("PData.txt", "a")

        first = False

        line = self.parseline(readfile.readline())



        #so this is setting the first set of values that will determine the first reference point



        s_time = int(float(line[0]))
        s_yaw = float(line[1])
        s_roll = float(line[2])
        s_pitch = float(line[3])
        s_accelx = float(line[4])
        s_accely = float(line[5])
        s_accelz = float(line[6])

        ref_x = 0
        ref_y = 0
        ref_z = 0


        while True:
            line = self.parseline(readfile.readline())

            if line[0] == '':
                break

            d_time = float(line[0])
            d_yaw = float(line[1])
            d_roll = float(line[2])
            d_pitch = float(line[3])
            d_accelx = float(line[4])
            d_accely = float(line[5])
            d_accelz = float(line[6])


            timedifference = (d_time - s_time) / 1000 #put it in seconds


            #vf = vi + at
            vf_x = s_accelx * timedifference
            vf_y = s_accely * timedifference
            vf_z = s_accelz * timedifference

            print("x velocity: " + str(vf_x) + " y velocity: " + str(vf_y) + " z velocity: " + str(vf_z))

            dx = (.5 * vf_x * timedifference) + ref_x
            dy = (.5 * vf_y * timedifference) + ref_y
            dz = (.5 * vf_z * timedifference) + ref_z

            print("x distance: " + str(dx) + " y distance: " + str(dy) + " z distance: " + str(dz))

            #Write points to another CSV file

            writefile.write(str(dx) + "," + str(dy) + "," + str(dz) + "\n")

            #update recursive values for the next iteration

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


csv = Csvparser("Data_Log.csv")