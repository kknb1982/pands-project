# Pands-project
# Introduction
This Readme gives an overview of the Python code used to create visual analyses of Fisher's Iris Dataset.  The journey towards this final code and an overview of the dataset is described in [Documentation.ipynb](https://github.com/kknb1982/pands-project/blob/main/Documentation.ipynb). 

# Table of contents
|Section number | Section title|Description|
|-------|-------|--------|
|[1](https://github.com/kknb1982/pands-project/blob/main/README.md#1-how-to-run-the-code) |How to run the code | |
|[2](https://github.com/kknb1982/pands-project/blob/main/README.md#2-analysispy) | Analysis.py| |
|[2.1](https://github.com/kknb1982/pands-project/blob/main/README.md#21-overview-of-analysispy)| Overview of analysis.py | |
|[2.2](https://github.com/kknb1982/pands-project/blob/main/README.md#22-the-code)| The code | |
|[3](https://github.com/kknb1982/pands-project/blob/main/README.md#3-variablemodulepy) | Variablemodule.py| |
|[3.1](https://github.com/kknb1982/pands-project/blob/main/README.md#31-overview-of-variable-modulepy)| Overview of variable module.py| |
|[3.2](https://github.com/kknb1982/pands-project/blob/main/README.md#32-the-code)|The code | |
|[4](https://github.com/kknb1982/pands-project/blob/main/README.md#4-references)| References| |

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
# 4. References
