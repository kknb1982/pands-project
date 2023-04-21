#
# Author: Kirstin Barnett

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
irisclass = "Class"

# Import Fisher's Iris dataset
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = (sepallen, sepalwid, petallen, petalwid, irisclass))

# Data analysis
datafields = sepallen, sepalwid, petallen, petalwid
def getdatainformation(data):
    for name in datafields:
        print (name)
        print (data[name].mean())
        print (data[name].min())
        print (data[name].max())
        print (data[name].median())
        print (" ")

print (getdatainformation(data))

data.plot(kind = 'scatter', x = sepallen, y = sepalwid)
plt.show()