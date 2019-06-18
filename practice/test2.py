
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#
def animate(i):
    xs = []
    ys = []
    x = randint(0,9)
    y = randint(0,9)
    xs.append(float(x))
    ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)
#

def animate(i):
    xs = []
    ys = []
    for z in range(100):
        x = randint(0,9)
        y = randint(0,9)
        print(x)
        print(y)
        xs.append(float(x))
        ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
'''


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("example.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()

