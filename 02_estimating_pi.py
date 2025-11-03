import matplotlib
import matplotlib.pyplot as plt
import random
NUM_POINTS=100000
count_in_circle=0

circle=plt.Circle((0,0), 1, color='r', fill=False)
box=plt.Rectangle((-1,-1), 2, 2, color='b', fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle)
ax.add_artist(box)
for i in range(NUM_POINTS):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<=1:
        ax.plot(x,y, 'yo',markersize=0.5)
        count_in_circle=count_in_circle+1
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
plt.show()

print(count_in_circle/NUM_POINTS*4)