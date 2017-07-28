print 1 + 2
print 1 + 3.5
print -1 + 2.5
print 100 - 45
print -1.1 + 5
print 3 * 2
print 3.5 * 1.5
print 3 / 2
print 4 / 2
print 3 // 2
print -3 // 2
print 9 % 2
print 2 ** 2
print 2 ** 10
print 1 ** 10
print 8 ** (1/3)
print 5 + 5 * 5
print (5 + 5) * 5
a = 3
print a + 1
a = 5
print a + 1
print type(3)
print type(3.5)
print type(3.0)
print int(3.8)
print int(3.0)
print float(3)
from fractions import Fraction
f = Fraction(3, 4)
print f
print Fraction(3, 4) + 1 + 1.5
print Fraction(3, 4) + 1 + Fraction(1/4)
a = 2 + 3j
print type(a)
a = complex(2, 3)
print a
b = 3 + 3j
print a + b
print a - b
print a * b
print a / b
z = 2 + 3j
print z.real
print z.imag
print z.conjugate()
print (z.real ** 2 + z.imag ** 2) ** 0.5
print abs(z)
a = input()
print a
s1 = 'a string'
s2 = "a string"
a = '1'
print int(a) + 1
print float(a) + 1
a = float(input())
a = input('Input an integer: ')
a = int(input())
print a + 1
a = int(input())
print 1.1.is_integer()
print 1.0.is_integer()
a = Fraction(input('Enter a fraction: '))
print a
z = complex(input('Enter a complex number: '))
print z
def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False
print is_factor(4, 1024)
for i in range(1, 4):
    print i
for i in range(5):
    print i
for i in range(1,10,2):
    print i
def factors(b):
    for a in range(1, b+1):
        if b % a == 0:
            print a
if __name__ == '__main__':
    b = input('Your Number Please: ')
    b = float(b)
    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')
item1 = 'apples'
item2 = 'bananas'
item3 = 'grapes'
print 'At the grocery store, I bought some {0} and {1} and {2}'.format(item1, item2, item3)
print 'Number 1: {0} Number 2: {1}'.format(1, 3.578)
def multi_table(a):
    for i in range(1,11):
        print '{0} x {1} = {2}'.format(a, i, a*i)

if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a))
print '{0}'.format(1.25456)
print '{0:.2f}'.format(1.25456)
print '{0:.2f}'.format(1.25556)
print '{0:.2f}'.format(1)
print 25.5 * 2.54 / 100
print 650 * 1.609
f = 98.6
print (f - 32) * (5 / 9)
c = 37
print c * (9 / 5) + 32

def print_menu():
    print '1. Kilometers to Miles'
    print '2. Miles to Kilometers'

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print 'Distance in miles: {0}'.format(miles)

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print 'Distance in kilometers: {0}'.format(km)

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
x = 10 - 500 + 79
print x
a = 1
b = 2
c = 1
d = (b**2 - 4*a*c)**0.5
x_1 = (-b + d)/(2*a)
x_2 = (-b - d)/(2*a)
print x_1, x_2
def roots(a, b, c):
    d = (b**2 - 4*a*c)**0.5
    x_1 = (-b + d)/(2*a)
    x_2 = (-b - d)/(2*a)
    print 'x1: {0}'.format(x_1)
    print 'x2: {0}'.format(x_2)

if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))
