x = 1
print x + x + 1
from sympy import Symbol
x = Symbol('x')
print x + x + 1
a = Symbol('x')
print a + a + 1
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
s = x*y + x*y
print s
p = x*(x + x)
print p
from sympy import factor, expand
expr = x**2 - y**2
print factor(expr)
factors = factor(expr)
print expand(factors)
expr = x**3 + 3*x**2*y + 3*x*y**2 + y**2
factors = factor(expr)
print factors
print expand(factors)
expr = x*y + x + y
print factor(expr)
expr = x*x + 2*x*y + y*y
print expr
from sympy import pprint
pprint(expr)
expr = 1 + 2*x + 2*x**2
pprint(expr)
from sympy import init_printing
init_printing(order='rev-lex')
pprint(expr)

def printseries(n):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)
if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    printseries(int(n))

print x*x + y*y + x*y + y*y
expr = x*x + y*y + x*y + y*y
res = expr.subs({x:1, y:2})
print res

print expr.subs({x:1-y})

expr_subs = expr.subs({x:1-y})
from sympy import simplify
print simplify(expr_subs)

def print_series(n, x_val):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)
    series_value = series.subs({x:x_val})
    print 'Value of the series at {0}: {1}'.format(x_val, series_value)

if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    x_value = input('Enter the value of x at which you want to evaluate the series: ')
    print_series(int(n), float(x_value))

from sympy import sympify
expr = input('Enter a mathematical expression: ')
expr = sympify(expr)
print 2 * expr

from sympy.core.sympify import SympifyError
expr = input('Enter a mathematical expression: ')
try:
    expr = sympify(expr)
except SympifyError:
    print 'Invalid Input'

from sympy import expand

def product(expr1, expr2):
    prod = expand(expr1 * expr2)
    print prod

if __name__ == '__main__':
    expr1 = input('Enter the first expression: ')
    expr2 = input('Enter the second expression: ')

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print 'Invalid Input'
    else:
        product(expr1, expr2)

from sympy import solve
x = Symbol('x')
expr = x - 5 - 7
print solve(expr)

expr = x**2 + 5*x + 4
print solve(expr, dict=True)

expr = x**2 + x + 1
print solve(expr, dict=True)

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

expr = a*x*x + b*x + c
print solve(expr, x, dict=True)

s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')
expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr,t, dict=True)
pprint(t_expr)

y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
print solve((expr1, expr2), dict=True)

soln = solve((expr1, expr2), dict=True)
soln = soln[0]
print expr1.subs({x:soln[x], y:soln[y]})
print expr2.subs({x:soln[x], y:soln[y]})

from sympy.plotting import plot
plot(2*x + 3)
plot((2*x + 3), (x, -5, 5))
plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3')
p = plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3', show=False)
p.save(line.png)

expr = input("Enter an expression with an 'x' and a 'y': ")
expr = sympify(expr)
y = Symbol('y')
print solve(expr, y)

solutions = solve(expr, 'y')
expr_y = solutions[0]
print expr_y

def plot_expression(expr):

    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)

if __name__ == '__main__':
    expr = input('Enter your expression in terms of x and y: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print 'Invalid Input'
    else:
        plot_expression(expr)

plot(2*x+3, 3*x+1)

p = plot(2*x+3, 3*x+1, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()
