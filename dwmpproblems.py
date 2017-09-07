import matplotlib.pyplot as p
def quadgraph():
    print 'equation format: ax^2 + bx + c'
    a = float(raw_input("pls type 'a' value: "))
    b = float(raw_input("pls type 'b' value: "))
    c = float(raw_input("pls type 'c' value: "))
    x_values = range(int(-1*b / 2*a - 40), int(-1*b / 2*a + 40))
    y_values = []
    for x in x_values:
        y = a * (x**2) + b*x + c
        y_values.append(y)
        print('x={0} y={1}'.format(x, y))
    p.plot(x_values, y_values)
    p.ylim([min(y_values), a * ((int(-1*b / 2*a) +10)**2) + b*(int(-1*b / 2*a) +10) + c])
    p.xlim([int(-1*b / 2*a - 10), int(-1*b / 2*a + 10)])
    p.show()
quadgraph()
