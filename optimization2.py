import numpy as np


# Define the function that we are interested in
def fun(x):
    return (np.sin(x[0]/2) + np.sin(x[1]/2))

# Make a grid to evaluate the function (for plotting)
x = np.linspace(-6, 6)
y = np.linspace(-6, 6)
xg, yg = np.meshgrid(x, y)

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(fun([xg, yg]), extent=[-6, 6, -6, 6], origin="lower",cmap="turbo")
plt.colorbar()

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xg, yg, fun([xg, yg]), rstride=1, cstride=1,
                       cmap=plt.cm.jet, linewidth=0, antialiased=False)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Six-hump Camelback function')

from scipy import optimize

x_min = optimize.minimize(fun, x0=[0, 0])

plt.figure()
# Show the function in 2D
plt.imshow(fun([xg, yg]), extent=[-6, 6, -6, 6], origin="lower",cmap="terrain")
plt.colorbar()
# And the minimum that we've found:
plt.scatter(x_min.x[0], x_min.x[1],marker=10, c='red')
print(x_min.x[0], x_min.x[1],fun([x_min.x[0], x_min.x[1]]))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xg, yg, fun([xg, yg]), rstride=1, cstride=1,
                       cmap='gist_rainbow', linewidth=0, antialiased=False)
ax.scatter(x_min.x[0], x_min.x[1],fun([x_min.x[0], x_min.x[1]]), marker=10,linewidths=20,c ="green")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Six-hump Camelback function')

plt.show()