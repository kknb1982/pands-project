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



print(data.corr())