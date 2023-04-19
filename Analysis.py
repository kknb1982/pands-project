#
# Author: Kirstin Barnett

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import Fisher's Iris dataset
colnames = "Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = colnames)
print (data.head(10))
#for name in colnames:
    #print (data[name].mean())
