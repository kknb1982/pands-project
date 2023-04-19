#
# Author: Kirstin Barnett

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from irisattributes import *
# Create the headers for the data fields as these aren't in the data file
colnames = ["sepal length", "sepal width", "petal length", "petal width", "class"]

# Import Fisher's Iris dataset
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = colnames)

# Data analysis
datafields = colnames[:-1]
def getdatainformation(data):
    for name in datafields:
        print (name)
        print (data[name].mean())
        print (data[name].min())
        print (data[name].max())
        print (data[name].median())
        print (" ")

print (getdatainformation(data))