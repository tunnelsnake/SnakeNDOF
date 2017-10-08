import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
z = [1,2,3,4,5,6,7,8,9]

ax1.plot_wireframe(x,y,z)

ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")




plt.show()