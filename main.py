import numpy
import pandas
import matplotlib.pyplot as plt

lowBoundary = -10000
highBoundary = 10000
numberOfElement = 1000
sampl = numpy.random.default_rng().uniform(lowBoundary, highBoundary, numberOfElement)
ser = pandas.Series(sampl, copy=False)
minValue = pandas.Series.min(ser)
maxValue = pandas.Series.max(ser)
sumValue = pandas.Series.sum(ser)

ser2 = pandas.Series(sampl, copy=False)
ser2.drop_duplicates()
countOfDublicates = ser.count() - ser2.count()

print(sampl)
print(f'Value min: {minValue}, value max {maxValue}, value sum {sumValue}, count of dublicates {countOfDublicates}')

print (f'Test {ser.count()}')

plot1 = plt.figure(1)
arrayX = list(range(1, numberOfElement + 1))
plt.plot(arrayX, ser)
plt.title('title name')
plt.xlabel('xAxis name')
plt.ylabel('yAxis name')

plot2 = plt.figure(2)
serFormatted = pandas.Series([float(round(elem, 2)) for elem in sampl], copy=False)
serFormatted.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Histograma for ')
plt.xlabel('Counts')
plt.ylabel('Values')
plt.grid(axis='y', alpha=0.75)
plt.show()