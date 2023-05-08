# Pands-project: Readme
# Introduction
This Readme gives an overview of the Python code used to create visual analyses of Fisher's Iris Dataset.  The journey towards this final code and an overview of the dataset is described in [Documentation.ipynb](https://github.com/kknb1982/pands-project/blob/main/Documentation.ipynb). 

# Table of contents
|Section number | Section title|
|-------|-------|
|[1](https://github.com/kknb1982/pands-project/blob/main/README.md#1-how-to-run-the-code) |How to run the code |
|[2](https://github.com/kknb1982/pands-project/blob/main/README.md#2-analysispy) | Analysis.py|
|[2.1](https://github.com/kknb1982/pands-project/blob/main/README.md#21-overview-of-analysispy)| Overview of analysis.py |
|[2.2](https://github.com/kknb1982/pands-project/blob/main/README.md#22-the-code)| The code |
|[3](https://github.com/kknb1982/pands-project/blob/main/README.md#3-variablemodulepy) | Variablemodule.py|
|[3.1](https://github.com/kknb1982/pands-project/blob/main/README.md#31-overview-of-variable-modulepy)| Overview of variable module.py|
|[3.2](https://github.com/kknb1982/pands-project/blob/main/README.md#32-the-code)|The code |
|[3.2.1](https://github.com/kknb1982/pands-project#321-import-the-libraries-needed)|Import the libraries needed|
|[3.2.2](https://github.com/kknb1982/pands-project#322-create-the-variable-names)|Create the variable names |
|[4](https://github.com/kknb1982/pands-project/blob/main/README.md#4-references)| References| 

# 1. How to run the code
To run the code use `python Analysis.py`. 

# 2. Analysis.py
## 2.1 Overview of analysis.py
This file uses the modules outlined in [variablemodule.py](https://github.com/kknb1982/pands-project/blob/main/variablemodule.py) to create a text file of simple statistical analyses of the variables in Fisher's Iris Dataset, histograms of the single variables and scatter plots of variable pairs. To enable meaningful analysis the plots are call coloured by the species of Iris.

## 2.2 The code
 The code starts by importing all the required modules and data from the variablemodule file.
    
    from variablemodule import *

This first module create a file and prints basic statistical information about each column to the file variabledata.txt

    printfielddata()

The next module creates simple histograms without colouring and saves them as combinehist.png to the github repository.
    
    createsimplehist()

These histograms without colouring by species are hard to read and only show the overall spread of the data, it does not help to decide which variables actually allow identification of the species. Therefore, there is a second module `gethisto()` creating individual plots, coloured by species.

The final module creates scatter plot for two variables.

    createpairplot()

# 3. Variablemodule.py
## 3.1 Overview of variable module.py
## 3.2 The code
### 3.2.1 Import the libraries needed
In order to analyse the data a few libraries are needed:
* `Pandas` to import the dataset and create the dataframe. 
* `Numpy` to create the statistical analyses of the data and support the creation of the plots. 
* `Matplotlib` to create the simple histograms without colouring by species. 
* `Seaborn` to create the coloured histograms and scatterplots.

The libraries have been imported using aliases to make the code more streamlined. 

  import pandas as pd 
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns 

### 3.2.2 Create the variable names
Fisher's Iris Dataset is published at https://archive.ics.uci.edu/ml/datasets/Iris/. The data is published without variable names and therefore, these need to be created to be used in our dataframe and code.

  sepallen = "Sepal Length"
  sepalwid = "Sepal Width"
  petallen = "Petal Length"
  petalwid = "Petal Width"
  species = "Species"

  datafields = sepallen, sepalwid, petallen, petalwid, species

### 3.2.3 Import Fishers Iris Dataset to a DataFrame
The code needs to import the Fisher's Iris Dataset and create a `DataFrame` using Pandas.

  dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

### 3.2.4 Finds the names of the iris species
Throughout the analysis it is useful to interrogate the data and plot it for each species separately. Therefore, we use the `Pandas` `unique()` method on teh column "species" to find out the unique values in this column. 

  irisspecies = dataf.Species.unique()

# Defines a function to creates a text file with summary data about the variable
def printfielddata():
    # Opens a text file called summary.txt to write data to, if it does not exist it will create it
    with open('summary.txt', 'w') as f:
        # iterate through the columns of the data
        for name in datafields:
            # Ignore species at this is not numerical data
            if name != species:
                header = (f'The column title is {name}')
                f.write(header)
                min = str(dataf[name].min())
                max = str(dataf[name].max())
                range = (f'\nThe minimum values is: {min} \nThe maximum value is: {max}')
                f.writelines(range)
                mean = str(dataf[name].mean())
                median = str(dataf[name].median())
                mode = str(dataf[name].mode())
                averages = (f'\nMean: {mean} \nMedian: {median} \nMode: {mode}\n\n')
                f.writelines(averages)              
            else:
                for x in irisspecies:
                    f.writelines(f'\n{x} \n')
                    x = dataf[dataf["Species"] == x]
                    describex = x.describe()
                    stringx = describex.to_string(header=True, index =True)
                    f.writelines(stringx) 
                f.close()

def createsimplehist():
    dataf.hist()
    plt.savefig('combinedhist.png')
    plt.close()

def gethisto():
    for name in datafields:
        if name != species:
            sns.histplot(data=dataf, x=name, hue=species, binwidth=0.1)
            plt.xlabel(f'{name} in cm')
            plt.title(f'Histogram of the relevant frequency of \n{name.lower()} highlighted by iris species')
            plt.savefig(name+ '.png')
            plt.close()

def createpairplot():
    sns.pairplot(dataf, hue=species)
    plt.savefig('pairplot.png')
    plt.close()
# 4. References
Pandas
Numpy
Matplotlib
Seaborn
UCI
Import data to dataframe
Pandas unique values
