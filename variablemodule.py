# File of all the functions required to read in Fisher's Iris Data Set and create the outputs requested
# Author: Kirstin Barnett

# Import the libraries needed
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Create the variable names
sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"

datafields = sepallen, sepalwid, petallen, petalwid, species

# Import Fishers Iris Dataset to a DataFrame
dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

# Finds the names of the iris species
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
    g= sns.pairplot(dataf, hue=species, diag_kind="hist")
    g.fig.subplots_adjust(left= .1, bottom=.1, top=.95)
    g.fig.suptitle('Pairplot of the variables in the Fisher Iris Dataset', fontsize = 16, fontweight='bold')
    g.fig.supxlabel('in cm')
    g.fig.supylabel('in cm')
    plt.savefig('pairplot.png')
    plt.close()

def getboxplots():
    dataf.boxplot(by=species, figsize=(11,11))
    plt.savefig('boxplot.png')
    plt.close()

chartvariables = datafields[:4]
def createboxsub():
    fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
    plt.suptitle("Box plots of Fisher Iris Dataset by Species")
    a = 1
    for name in chartvariables:
        plt.subplot(2,2,a)
        sns.boxplot(data=dataf, x=species, y=name)
        plt.ylabel(f'{name} in cm')
        a += 1
    else:
        plt.savefig('boxsub.png')

def getviolinplots():
    for name in datafields:
        if name != species:
            sns.violinplot(data=dataf, x=species, y=name)
            plt.ylabel(name+ 'in cm')
            plt.title(f'Violin plot of {name} in cm separated by species')
            plt.savefig(name+ 'violin.png')
            plt.close()