from math import pi, ceil
import turtle
import sys
t = turtle.Pen()
t.speed(0)
t.color('blue')
t.backward(100)
t.color('black')
t.lt(90)
t.fd(50)
t.circle(-50, 180)
t.color('red')
t.fd(50)
t.color('green')
t.lt(120)
t.fd(200)
t.color('black')
t.lt(60)
t.fd(50)
t.circle(50, 120)
t.lt(0)
t.fd(200)
t.up()
t.fd(1000)
print ''
print ''
print ''
print 'WELCOME TO THE BEST PROGRAM EVER v2'
print 'TODAY WE WILL BE FINDING THE DIMENSIONS OF THE PLATIC SHEET\nTHAT YOU WILL NEED TO COVER YOUR GREENHOUSE'
print 'THE DRAWING REPRESENTS THE GREENHOUSE'
print ''
try:
    x = int(raw_input('PLEASE INPUT THE LENGTH OF THE RED SEGMENT OF YOUR GREENHOUSE(IN INCHES): '))
    y = int(raw_input('PLEASE INPUT THE LENGTH OF THE BLUE SEGMENT OF YOUR GREENHOUSE(IN FEET): '))
    z = int(raw_input('PLEASE INPUT THE LENGTH OF THE GREEN SEGMENT OF YOUR GREENHOUSE(IN FEET): '))
except ValueError:
    print ''
    print 'TRY AGAIN. THE NUMBER YOU INPUTTED WAS WRONG'
    sys.exit()
length = ceil(float(2 + 2 * (x/12) + y + z) / 5) * 5
width = ceil(float(2 + 2 * (x/12)  + .5 * y * pi) / 5) * 5
print ''
print ''
print ''
print 'You will need a ' + str(int(length)) + '\' by ' + str(int(width)) + '\' sheet to sheet your greenhouse.'
