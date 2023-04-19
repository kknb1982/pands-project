#
# Author: Kirstin Barnett

import pandas as pd
import matplotlib as plt
import numpy as np

# Import Fisher's Iris dataset
colnames = "Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = colnames)

for name in colnames:
    print (iris[name].mean())
