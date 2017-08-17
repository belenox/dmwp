import sys
h = 6.62606876 * 10 ** -34
print ''
print 'WELCOME TO THE BEST PROGRAM EVER'
print 'THIS PROGRAM WILL ROCK YOUR WORLD'
print 'ITS GONNA CALCULATE WAVES AND STUFF'
print 'ALL YOU GOTTA DO IS INPUT A NUMBER'
print 'IN SCIENTIFIC NOTATION'
print ''
E = raw_input('Input the E value in scientific notation (e.g. 4.35 e-23): ')
try:
    print '\n\nWOW'
    print 'YOUR SOCKS ARE GONNA BE KNOCKED OFF'
    print 'CUZ THIS PROGRAM IS ABOUT TO GIVE YOU THE WAVELENGTH'
    print 'AND THE FREQUENCY OF THAT WAVE'
    print ''
    E = E.split()
    roundto = 0
    dot = False
    for a in E[0]:
        if dot == True: roundto += 1
        if a == '.': dot = True

    E[1] = E[1][1:]
    E = float(E[0]) * 10 ** int(E[1])
    v = E / h
    v = str(v)
    C = 299792458.0
    l = C / float(v)
    l = str(l)
    visL = 7 * 10 ** -7
    UV = 38 * 10 ** -8
    l = str(round(float(l[0: len(l) - 4]), roundto)) + l[len(l) - 4:]
    v = str(round(float(v[0: len(v) - 4]), roundto)) + v[len(v) - 4:]
    if l > visL:
        print ''
        print 'THESE ARE THE ANSWERS'
        print ''
        print 'The frequency of the wave is ' + str(v) + '/second.'
        print 'The wavelength of the wave is ' + str(l) + ' meters'
        print 'Type: Infrared'
        print ''
        print 'THEY ARE SO CORRECT'
        print ''
    elif l > UV:
        print ''
        print 'THESE ARE THE ANSWERS'
        print ''
        print 'The frequency of the wave is ' + str(v) + '/second.'
        print 'The wavelength of the wave is ' + str(l) + ' meters'
        print 'Type: Visible Light'
        print ''
        print 'THEY ARE SO CORRECT'
        print ''
    else:
        print ''
        print 'THESE ARE THE ANSWERS'
        print ''
        print 'The frequency of the wave is ' + str(v) + '/second.'
        print 'The wavelength of the wave is ' + str(l) + ' meters'
        print 'Type: Ultra Violet'
        print ''
        print 'THEY ARE SO CORRECT'
        print ''
except IndexError:
    sys.exit('YOU ARE DUMB.  YOU PUT IN THE VALUE WRONG.  GO TO SCHOOL AND COME BACK LATER')
