# Creates a text file with basic statistical information about the variables. 
# Creates histograms of the variables
# Prints scatter plots of variable pairs

# Author: Kirstin Barnett

from variablemodule import *

# Creates a file and prints basic statistical information about each column to the file variabledata.txt
printfielddata()

# Creates histograms of each variable
createsimplehist()
gethisto()

# Creates scatter plot for two variables
createpairplot()

# Creates boxplot
getboxplots()