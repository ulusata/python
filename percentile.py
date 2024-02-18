import numpy as np

#Percentile are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentileValue = np.percentile(ages, 75)
print(percentileValue) #43
#It means that %75 of people are 43 are lower than that.

percentileValue = np.percentile(ages, 90)
print(percentileValue) #61
#It means %90 of people are under 61.