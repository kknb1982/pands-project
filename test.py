import pandas as pd
sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
irisclass = "Class"

colnames = sepallen + sepalwid
print (colnames)

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = (sepallen, sepalwid, petallen, petalwid, irisclass))

print(data.head())