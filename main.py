import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lowBoundary = -10000
highBoundary = 10000
numberOfElement = 1000

# содаем данные, случайные значения
sample = np.random.default_rng().uniform(lowBoundary, highBoundary, numberOfElement)

# содаем series
ser = pd.Series(sample, copy=False)

# максимальное значение
minValue = pd.Series.min(ser)

# минимальное значение
maxValue = pd.Series.max(ser)

# сумма
sumValue = pd.Series.sum(ser)

# содаем series
ser2 = pd.Series(sample, copy=False)

# убираем повторяющиеся значения
ser2.drop_duplicates()

# ищем число повторяющихся
countOfDuplicates = ser.count() - ser2.count()

print(f'sample: {sample}')
print(f'Value min: {minValue}, value max : {maxValue}, value sum : {sumValue}, count of duplicates : {countOfDuplicates}')

# график
plot1 = plt.figure(1)
arrayX = list(range(1, numberOfElement + 1))
plt.plot(arrayX, ser)
plt.title('Result')
plt.xlabel('Numbers')
plt.ylabel('Values')

# гистограмма
plot2 = plt.figure(2)
serFormatted = pd.Series([float(round(elem, 2)) for elem in sample], copy=False)
serFormatted.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Histogram for values')
plt.xlabel('Counts')
plt.ylabel('Values')
plt.grid(axis='y', alpha=0.75)

# Сортировка по убыванию
serDesc = ser.sort_values(ascending=False)
# Сортировка по возрастанию
serAsc = ser.sort_values()

dataDict = {
    'source': ser,
    'ascended': serAsc.tolist(),
    'descended': serDesc.tolist()
}

# дата фрейм
dataFrame = pd.DataFrame(data=dataDict)
print(f'Data frame : {dataFrame}')

# графики убывания и возрастания
plot3 = plt.figure(3)
plt.plot(arrayX, serAsc)
plt.plot(arrayX, serDesc)
plt.title('Ascending and descending')
plt.xlabel('Number')
plt.ylabel('Value')

plt.show()
