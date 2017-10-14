__author__ = "Jacob Thomas"

import math

class Euler_transform():


    def __init__(self, theta, psi, phy, inputfile='logs/pointdata.csv', outputfile='logs/matrixdata.csv'):
        r = open(inputfile, 'r')

        #clear out the logfile
        w = open(outputfile, 'w').close()
        w = open(outputfile, 'a')

        while True:

            pointstr = r.readline()
            pointlist = str.split(pointstr, ",")

            if pointlist[0] == "":
                break

            x = float(pointlist[0])
            y = float(pointlist[1])
            z = float(pointlist[2])

            x, y, z = self.apply_matrix(x, y, z, float(theta), float(psi), float(phy))
            w.write(str(x) + "," + str(y) + "," + str(z) + "\n")


    def apply_matrix(self, x, y, z, theta, psi, phy):

        # ROTATION MATRICES

        # apply x rotation matrix in derived form
        if theta != 0 and theta % 360 != 0:
            x = x
            y = (y * math.cos(math.radians(theta))) + (y * -math.sin(math.radians(theta)))
            z = (y * math.sin(math.radians(theta))) + (z * math.cos(math.radians(theta)))

        # apply y rotation matrix
        if psi != 0 and psi % 360 != 0:
            x = (x * math.cos(math.radians(psi))) + (z * math.sin(math.radians(psi)))
            y = y
            z = (x * -math.sin(math.radians(psi))) + (z * math.cos(math.radians(psi)))

        # apply z rotation matrix
        if phy != 0 and phy % 360 != 0:
            x = (x * math.cos(math.radians(phy))) + (y * -math.sin(math.radians(phy)))
            y = (y * math.sin(math.radians(phy))) + (y * math.cos(math.radians(phy)))
            z = z

        return x, y, z




