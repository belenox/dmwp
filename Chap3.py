shortlist = [1, 2, 3]
print sum(shortlist)
print len(shortlist)
def calculate_mean(numbers):
    s = float(sum(numbers))
    N = float(len(numbers))
    mean = s/N
    return mean
print calculate_mean([1, 2])
if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    print 'Mean donations over the last {0} days is {1}'.format(len(donations), calculate_mean(donations))
samplelist = [4, 1, 3]
samplelist.sort()
print samplelist
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1
        median = (numbers[int(m1) - 1] + numbers[int(m2) - 1]) / 2
    else:
        median = numbers[((N+1) / 2) - 1]
    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    print 'Median donation over the last {0} days is {1}'.format(len(donations), calculate_median(donations))

simplelist = [4, 2, 1, 3, 4]
from collections import Counter
c = Counter(simplelist)
print c.most_common()
print c.most_common(1)
print c.most_common(2)
mode = c.most_common(1)
print mode
print mode[0]
print mode[0][0]

def calculate_mode(numbers):
    return Counter(numbers).most_common(1)[0][0]

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores)

print 'The mode of the list of numbers is: {0}'.format(mode)

def calculate_mode(numbers):
    c = Counter(numbers).most_common()
    max_count, modes = c[0][1], []
    for num in c:
        if num[1] == max_count: modes.append(num[0])
    return modes

if __name__ == '__main__':
    scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
    modes = calculate_mode(scores)
    print 'The mode(s) of the list of numbers are: '
    for mode in modes: print mode

def frequency_table(numbers):
    table = Counter(numbers)
    print 'Number\tFrequency'
    for number in table.most_common():
        print '{0}\t{1}'.format(number[0], number[1])

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)

def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    print('Number\tFrequency')
    for number in numbers_freq:
        print '{0}\t{1}'.format(number[0], number[1])

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)

def find_range(numbers):
    low = min(numbers)
    high = max(numbers)
    r = high - low
    return low, high, r

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):
    for x in range(len(numbers)): numbers[x] = float(numbers[x])
    diff = find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    variance = sum(squared_diff)/len(numbers)
    return variance

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

std = variance**0.5
print 'The standard deviation of the list of numbers is {0}'.format(std)

simplelist1 = [1, 2, 3]
simplelist2 = [4, 5, 6]
for x, y in zip(simplelist1, simplelist2):
    print x, y

def findcorrxy(x, y):
    n = len(x)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)
    sumprodxy = sum(prod)
    sumx = sum(x)
    sumy = sum(y)
    squaredsumx = sumx**2
    squaredsumy = sumy**2
    xsquare = []
    for xi in x:
        xsquare.append(xi**2)
    xsquaresum = sum(xsquare)
    ysquare = []
    for yi in y:
        ysquare.append(yi**2)
    ysquaresum = sum(ysquare)
    numerator = n*sumprodxy - sumx*sumy
    denominatorterm1 = n*xsquaresum - squaredsumx
    denominatorterm2 = n*ysquaresum - squaredsumy
    denominator = (denominatorterm1 * denominatorterm2)**0.5
    correlation = numerator/denominator
    return correlation

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.scatter(x, y)
plt.show()

def sumdata(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s = s + float(line)
    print 'Sum of the numbers: {0}'.format(s)

if __name__ == '__main__':
    sumdata('mydata.txt')

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    return numbers

if __name__ == '__main__':
    data = read_data('mydata.txt')
    mean = calculate_mean(data)
    print 'Mean: {0}'.format(mean)

import csv

def scatterplot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()

def read_csv(filename):
    numbers = []
    squared = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
            squared.append(int(row[1]))
        return numbers, squared

if __name__ == '__main__':
    numbers, squared = read_csv('numbers.csv')
    scatterplot(numbers, squared)

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[0]))
            highest_correlated.append(float(row[1]))

        return summer, highest_correlated

if __name__ == '__main__':
    summer, highest_correlated = read_csv('numbers.csv')
    corr = findcorrxy(summer, highest_correlated)
    print 'Highest correlation: {0}'.format(corr)
    scatterplot(summer, highest_correlated)
