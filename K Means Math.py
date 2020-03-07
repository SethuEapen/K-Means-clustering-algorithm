import numpy as np
from random import randint
import matplotlib.pyplot as plt
from matplotlib import style

x = []
y = []

#set centroids to random values
centroids = np.array([[randint(0,250),randint(0,250)],
                      [randint(0,250),randint(0,250)],
                      [randint(0,250),randint(0,250)]])

c1 = []
c2 = []
c3 = []
C1x = []
C2x = []
C3x = []
C1y = []
C2y = []
C3y = []
changing = True

for i in range(30):
    x.append(randint(0,100))
    y.append(randint(0,100))
    x.append(randint(150, 250))
    y.append(randint(0, 100))
    x.append(randint(150, 250))
    y.append(randint(150, 250))

def draw():
    for i in centroids:
        plt.scatter(i[0], i[1], 140, marker="d", edgecolors="black")
    plt.scatter(C1x, C1y, c="black")
    plt.scatter(C2x, C2y, c="red")
    plt.scatter(C3x, C3y, c="green")
    plt.show()

def assign_Point():
    c1.clear();c2.clear();c3.clear()
    for pnt in range(len(x)):#for each point in the grid
        distances = []
        for i in centroids:
            #find distance to point using equation (2.1)
            distances.append(((i[0] - x[pnt]) ** 2 + (i[1] - y[pnt]) ** 2) ** 0.5)

        #what is the nearest distance
        nearest = distances.index(min(distances))

        #assign the point to its closest centroid
        if nearest == 0:
            c1.append(pnt)
        elif nearest == 1:
            c2.append(pnt)
        else:
            c3.append(pnt)
    mod() #run function to create arrays with (x,y) coordenates for each centroid
    #arrays called C1x, C1y, C2x, C2y, C3x, C3y

def mod():
    C1x.clear();C1y.clear();C2x.clear();C2y.clear();C3x.clear();C3y.clear()
    for i in c1:
        C1x.append(x[i])
        C1y.append(y[i])
    for i in c2:
        C2x.append(x[i])
        C2y.append(y[i])
    for i in c3:
        C3x.append(x[i])
        C3y.append(y[i])

def move_centroid():
    old_centroids = centroids.copy()
    #recenter the centroid at mean of dimention
    #effective use of equation (3.1)
    if len(c1) != 0:
        (centroids[0])[0] = np.mean(C1x)
        (centroids[0])[1] = np.mean(C1y)
    if len(c2) != 0:
        (centroids[1])[0] = np.mean(C2x)
        (centroids[1])[1] = np.mean(C2y)
    if len(c3) != 0:
        (centroids[2])[0] = np.mean(C3x)
        (centroids[2])[1] = np.mean(C3y)
    #Did the centroids move?
    comparison = old_centroids == centroids
    if comparison.all():
        #if they didnt move return false to end program
        return False
    else:
        return True
        #if they did move return true to keep going

assign_Point()

print(c1)
print(c2)
print(c3)
draw()
count = 0
while changing: #continue running while changing variable is true
    count = count + 1 #add count to measure # of itterations
    assign_Point() #assign the points to closest centroids
    changing = move_centroid()#update centroid location
    #if the centroids didnt move and function returned False end program
    #if count % 5 == 0:
    print(count)
    draw() #display updated graph on screen

print("Final Count: " + str(count))
draw()
