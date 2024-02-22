import pandas
from sklearn import linear_model

#Multiple Regression
#We try to predict a value based on two or more variables.

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']] #Independent
y = df['CO2'] #Dependent

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2) #107.2087

print(regr.coef_) #0.00755095, 0.00780526
#These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
#And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.

predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2) #114.7596