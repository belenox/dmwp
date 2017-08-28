import pylab as p
hybrid = 'Ford Fusion S Hybrid'
nonhybrid = 'Ford Fusion S'
hprice = 25295
nhprice = 22120
hmpg = 42
nhmpg = 26.5
avgfuel = 2.24

cpmh = avgfuel/hmpg
cpmnh = avgfuel/nhmpg
xint = int((hprice - nhprice)/(cpmnh - cpmh))
yint = int(xint * cpmh + hprice)
xvals = [0, 1e5/4, 2e5/4, 3e5/4, 4e5/4, 5e5/4]
hcosts = [hprice, hprice+(cpmh * 1e5/4), hprice+(cpmh * 2e5/4), hprice+(cpmh * 3e5/4), hprice+(cpmh * 4e5/4), hprice+(cpmh * 5e5/4)]
nhcosts = [nhprice, nhprice+(cpmnh * 1e5/4), nhprice+(cpmnh * 2e5/4), nhprice+(cpmnh * 3e5/4), nhprice+(cpmnh * 4e5/4), nhprice+(cpmnh * 5e5/4)]
p.plot(xvals, hcosts, xvals, nhcosts)
p.xlabel('Miles')
p.ylabel('Total Cost')
p.legend(['Hybrid', 'Non-Hybrid'])
p.figtext(.02, .935, 'The hybrid car is a ' + hybrid + '.\nThe non-hybrid car is a ' + nonhybrid + '.')
p.figtext(0.42, 0.935, 'The x value of the intersection for miles is ' + str(xint) + '\nThe y value of the intersection for cost in dollars is ' + str(yint))
p.show()
