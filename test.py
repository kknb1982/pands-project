import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from variablemodule import *
from fielddatamodule import getfielddata

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"

datafields = sepallen, sepalwid, petallen, petalwid, species

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

with open('variabledata.txt', 'a') as f:
    f.write("This is a file summarising details about the variables in Fisher's Iris Data Set")
    f.write(getfielddata())
    f.close()