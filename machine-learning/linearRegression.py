import matplotlib.pyplot as plt
from scipy import stats

#The term regression is used when you try to find the relationship between variables.
#In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def prediction(x):
    return slope * x + intercept

mymodel = list(map(prediction, x))
#plt.scatter(x, y)
# plt.plot(x, prediction)
#plt.show()

print(r) #-0.7585 It means it is not a perfect relation but we can use it to predict some future outcomes.

predictedSpeed = prediction(5) #We are trying to figure out how fast is a 5 years old car.
print(predictedSpeed) #94.3495