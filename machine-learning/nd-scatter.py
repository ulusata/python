from numpy import random
import matplotlib.pyplot as plt

#Normal data distribution
dataSet = random.normal(80, 6, 810)
#plt.hist(dataSet, 81)


#Scatter distribution
age = [5,7,8,7,2,17,2,9,4,11,12,9,6]
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#plt.scatter(age, speed)
#plt.show()

age = random.normal(9, 2, 1000)
speed = random.normal(100, 10, 1000)
plt.scatter(age, speed)
plt.show()