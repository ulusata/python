import numpy as np
from scipy import stats

#Mean: The average value
#Median: The mid point value
#Mode The most common value

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

meanValue = np.mean(speed)
print(meanValue) #89.7692

medianValue = np.median(speed)
print(medianValue) #87

modeValue = stats.mode(speed)
print(modeValue) #mode=86, count=3

#Standart deviation is a number that describes how spread out the values are
#A low standart deviation means most of the values are close to mean value(average) and with high standart deviation it is vice versa.

stdValue = np.std(speed)
print(stdValue) #9.2582