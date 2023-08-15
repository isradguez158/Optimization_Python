import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D

#fig = plt.figure(figsize=(10,10))
#axes = fig.gca(projection='3d')
fig, axes = plt.subplots(subplot_kw={"projection": "3d"})

def f(x, y):
    return (np.sin(x/2) + np.sin(y/2))

y = x = np.linspace(-6, 6, 50)

x, y = np.meshgrid(x, y)
z = f(x,y)


# optimization x
optimization = optimize.minimize(f, [-6], args=(-6,)) 
best_x = optimization.x

# optimization y
optimization = optimize.minimize(lambda x,y: f(y,x), [-6], args=(-6,))
best_y = optimization.x

#surf = axes.plot_surface(x, y, z, cmap='coolwarm',linewidth=0, antialiased=True)
axes.plot_surface(x, y, z, cmap='plasma',\
                edgecolor='black')
axes.scatter3D([best_x], [best_y], [f(best_x, best_y)], s=[100], c="g")


axes.set_xlabel('Ось X')
axes.set_ylabel('Ось Y')
axes.set_zlabel('Ось Z')

plt.show()