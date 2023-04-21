import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"

datafields = sepallen, sepalwid, petallen, petalwid, species

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

print (data.head())

for name in datafields:
    if name != species:
        print (name)
        min = data[name].min()
        max = data[name].max()
        print("Minimum: ", min, "\nMaximum: ", max)
        mean = data[name].mean()
        median = data[name].median()
        mode = data[name].mode()
        print("Mean: ", mean,"\nMedian: ", median, "\nMode: ", mode)
        name = data[[name, species]]
        print (name.head())
     
    else: 
        break

print(data.corr())