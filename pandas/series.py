import pandas as pd

myDataSet = {
        'cars': ['BMW', 'Volvo', 'Ford'],
        'passings': [3, 5, 7]
    }

myvar = pd.DataFrame(myDataSet)
#print(myvar)

#print(pd.__version__)

a = [3, 5, 6]
myvar = pd.Series(a)
#print(myvar)
#print(myvar[1])

myvar = pd.Series(a, index = ['x', 'y', 'z'])
#print(myvar)
#print(myvar['x'])

marks = {'student1': 95, 'student2': 80, 'student3': 65}
myvar = pd.Series(marks)
#print(myvar)
#print(myvar['student2'])
#The keys of the marks dictionary become the labels of the pandas series.

data = {
        'students': ['Alice', 'John', 'Melissa', 'Jack', 'Joe', 'Alex'],
        'marks': [100, 90, 76, 45, 87, 82]
    }
indexNumbers = [x for x in range(1, 7)]
myvar = pd.DataFrame(data, index = indexNumbers)
print(myvar)