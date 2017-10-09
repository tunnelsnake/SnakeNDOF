import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


class Data_plot():

    def __init__(self, file):

        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')

        try:
            f = open(file, "r")
        except IOError:
            print("An Error Occurred Opening File " + file)


        x = list("")
        y = list("")
        z = list("")

        pointstr = f.readline()
        while True:

            pointlist = str.split(pointstr, ",")
            if pointlist[0] == "":
                break
            x.append(float(pointlist[0]))
            y.append(float(pointlist[1]))
            z.append(float(pointlist[2]))

            pointstr = f.readline()

        ax1.plot_wireframe(x, y, z)

        ax1.set_xlabel("X")
        ax1.set_ylabel("Y")
        ax1.set_zlabel("Z")

        plt.show()