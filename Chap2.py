simplelist = [1, 2, 3]
print simplelist[0]
print simplelist[1]
print simplelist[2]
stringlist = ['a string', 'b string', 'c string']
print stringlist[0]
print stringlist[1]
print stringlist[2]
emptylist = []
print emptylist
emptylist.append(1)
print emptylist
emptylist.append(2)
print emptylist
simpletuple = (1, 2, 3)
print simpletuple[0]
print simpletuple[1]
print simpletuple[2]
l = [1, 2, 3]
for item in l:
    print item
for index, item in enumerate(l):
    print(index, item)

x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]
from pylab import plot, show
plot(x_numbers, y_numbers)
show()
plot(x_numbers, y_numbers, marker='o')
show()
plot(x_numbers, y_numbers, 'o')
show()
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker='o')
show()
nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nyc_temp, marker='o')
show()
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
show()
plot(months, nyc_temp_2000)
plot(months, nyc_temp_2006)
plot(months, nyc_temp_2012)
show()
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
from pylab import legend
legend([2000, 2006, 2012])
show()
from pylab import plot, show, title, xlabel, ylabel, legend
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
title('Average monthly temperature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])
from pylab import axis
axis()
axis(ymin=0)
show()
import matplotlib.pyplot
def create_graph():
    x_numbers = [1, 2, 3]
    y_numbers = [2, 4, 6]

    matplotlib.pyplot.plot(x_numbers, y_numbers)
    matplotlib.pyplot.show()

if __name__ == '__main__':
    create_graph()

import matplotlib.pyplot as plt
def create_graph():
    x_numbers = [1, 2, 3]
    y_numbers = [2, 4, 6]

    plt.plot(x_numbers, y_numbers)
    plt.show()

if __name__ == '__main__':
    create_graph()

from pylab import plot, savefig
x = [1, 2, 3]
y = [2, 4, 6]
plot(x, y)
savefig('mygraph.png')

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force and distance')
    plt.show()

def generate_f_r():
    r = range(100, 1001, 50)
    f = []

    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        f.append(force)
    draw_graph(r, f)

if __name__ == '__main__':
    generate_f_r()

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    return numbers
from matplotlib import pyplot as plt
import math
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers
def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    t_flight = 2*u*math.sin(theta)/g
    intervals = frange(0, t_flight, 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)

if __name__ == '__main__':
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
    draw_trajectory(u, theta)
    plt.show()

if __name__ == '__main__':
    u_list = [20, 40 ,60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
    plt.legend(['20', '40', '60'])
    plt.show()
