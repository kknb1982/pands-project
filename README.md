# Pands-project
# Introduction
<<<<<<< HEAD
This Readme gives an overview of the Python code used to create visual analyses of Fisher's Iris Dataset.  The journey towards this final code and an overview of the dataset is described in Documentation.ipynb. 

# Table of contents
|Section title|Description|
|-------|--------|
|How to run the code(https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-1---prints-out-hello-world)| week1.helloworld.py|Prints out "Hello World!"|
|[02](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-2---adds-two-user-entered-amounts-and-prints-them-in-a-readable-format)|week2.bank.py| Adds two user entered integers and ouputs them in euro and cents|
|[03](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-3---hiding-part-of-bank-account-numbers)|week3.accounts.py|Hiding part of bank account numbers|
|[04](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-4---coding-the-collatz-conjecture)|week4.collatz.py|Coding the collatz conjecture|
|[05](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-5---using-import-to-work-out-if-today-is-a-weekday)|week5.weekday.py|Outputs whether today is a weekday or not and prints out appropriate text|
|[06](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-6---finds-an-approximation-of-the-square-root-of-a-positive-float-number)|week6.sqrt.py|Finds an approximation of the square root of a positive float number|
|[07](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-7---counting-the-occurence-of-a-character-in-a-file)|week7.files.py|Counting the occurence of a character in a file|
|[08](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-8)|week8.plottask.py|Plot of the normal distribution and a cubing function|

# How to run the code
# Overview of Analysis.py
## The code
# Overview of Variablemodule.py
## The code

# References
=======
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
>>>>>>> 4d4da3dec6e2edb26976438cc308299e8a48f09e
