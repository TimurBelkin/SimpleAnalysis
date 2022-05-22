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

print(f'Sample: {sampl}')
print(f'Value min: {minValue}, value max {maxValue}, value sum {sumValue}, count of dublicates {countOfDublicates}')

plot1 = plt.figure(1)
arrayX = list(range(1, numberOfElement + 1))
plt.plot(arrayX, ser)
plt.title('Result')
plt.xlabel('Numbers')
plt.ylabel('Values')

plot2 = plt.figure(2)
serFormatted = pandas.Series([float(round(elem, 2)) for elem in sampl], copy=False)
serFormatted.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Histogram for values')
plt.xlabel('Counts')
plt.ylabel('Values')
plt.grid(axis='y', alpha=0.75)


serDesc = ser.sort_values(ascending=False)
serAsc = ser.sort_values()

plot3 = plt.figure(3)
plt.plot(arrayX, serAsc)
plt.plot(arrayX, serDesc)
plt.title('Ascending and descending')
plt.xlabel('Number')
plt.ylabel('Value')

plt.show()