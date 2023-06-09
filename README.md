# Pands-project: Readme
# Introduction
This Readme gives an overview of the Python code used to create visual analyses of Fisher's Iris Dataset.  The journey towards this final code and an overview of the dataset is described in [Documentation.ipynb](https://github.com/kknb1982/pands-project/blob/main/Documentation.ipynb). 

# Table of contents
|**Section number** | **Section title**|
|-------|-------|
|**[1](https://github.com/kknb1982/pands-project/blob/main/README.md#1-how-to-run-the-code)** |**How to run the code** |
|[1.1](https://github.com/kknb1982/pands-project/tree/main#11-what-else-is-in-the-repository)|What else is in the repository?|
|**[2](https://github.com/kknb1982/pands-project/blob/main/README.md#2-analysispy)** | **Analysis.py**|
|    [2.1](https://github.com/kknb1982/pands-project/blob/main/README.md#21-overview-of-analysispy)| Overview of analysis.py |
|    [2.2](https://github.com/kknb1982/pands-project/blob/main/README.md#22-the-code)| The code |
|**[3](https://github.com/kknb1982/pands-project/blob/main/README.md#3-variablemodulepy)**| **Variablemodule.py**|
|  [3.1](https://github.com/kknb1982/pands-project/blob/main/README.md#31-overview-of-variable-modulepy)| Overview of variable module.py|
|  [3.2](https://github.com/kknb1982/pands-project/blob/main/README.md#32-the-code)|The code |
|   [3.2.1](https://github.com/kknb1982/pands-project#321-import-the-libraries-needed)|Import the libraries needed|
|   [3.2.2](https://github.com/kknb1982/pands-project#322-create-the-variable-names)|Create the variable names |
|   [3.2.3](https://github.com/kknb1982/pands-project/blob/main/README.md#323-import-fishers-iris-dataset-to-a-dataframe)|Import Fishers Iris Dataset to a DataFrame|
|   [3.2.4](https://github.com/kknb1982/pands-project/blob/main/README.md#324-finds-the-names-of-the-iris-species)|Finds the names of the iris species |
|   [3.2.5]()|Defines a function to create a text file with summary data about the variable|
|   [3.2.6](https://github.com/kknb1982/pands-project/blob/main/README.md#326-create-simple-histograms)|Create simple histograms |
|   [3.2.7](https://github.com/kknb1982/pands-project/blob/main/README.md#327-create-histograms-coloured-by-species)|Create histograms coloured by species |
|   [3.2.8](https://github.com/kknb1982/pands-project/blob/main/README.md#328-create-scatterplots)|Create scatterplots|
|   [3.2.9](https://github.com/kknb1982/pands-project/blob/main/README.md#329-create-boxplots)|Create boxplots|
|   [3.2.10](https://github.com/kknb1982/pands-project/blob/main/README.md#3210-creating-boxplots-using-the-subplot-method)|Creating boxplots using the subplot method|
|   [3.2.11](https://github.com/kknb1982/pands-project/blob/main/README.md#3210-create-violinplots)|Create violinplots|
|**[4](https://github.com/kknb1982/pands-project/tree/main#4-further-reading-and-information)**|Further reading and information|
|**[5](https://github.com/kknb1982/pands-project/tree/main#5-references)**| **References**| 

# 1. How to run the code
To run the code use `python Analysis.py`. 

## 1.1 What else is in the repository?
The repository on github (https://github.com/kknb1982/pands-project) includes both the code and the output files. The code and how the file contents are created are described in later sections of this Readme, but here is a brief explanation of each file:
* **Analysis.py:** This is the file to run to create the dataframe and plots
* **boxplot.png:** This is a boxplot of the Fisher Iris Dataset separated by species.
* **boxsub.png:** This is another boxplot of the Fisher Iris Dataset separated by species. This plot has been created using the subplot method for a better layout.
* **Descriptor.ipynb:** This gives an explanation of the Fisher Iris Dataset, techniques for analysing data visually and explains the journey towards my final code.
* **pairplot.png:** This shows of plot of all variable pairs as scatter plots and univariate plots as histograms.
* **Petal Length.png:** This is a histogram of the Petal Length data split by Species of Iris.
* **Petal Lengthviolin.png:** This is a violin plot of the Petal Length data split by Species of Iris.
* **Petal Width.png:** This is a histogram of the Petal Width data split by Species of Iris.
* **Petal Widthviolin.png:** This is a violin plot of the Petal Width data split by Species of Iris.
* **Sepal Length.png:** This is a histogram of the Sepal Length data split by Species of Iris.
* **Sepal Lengthviolin.png:** This is a violin plot of the Sepal Length data split by Species of Iris
* **Sepal Width.png:** This is a histogram of the Sepal Width data split by Species of Iris
* **Sepal Widthviolin.png:** This is a violin plot of the Sepal Width data split by Species of Iris
* **summary.txt:** This text file gives details about the Iris Fisher dataset.
* **variablemodule.py:** This is the code for importing the dataset, setting variables and the functions to create the plots.
* **Ztest.txt:** This is the test file for writing to files used by the Descriptor notebook. This can be ignored.

# 2. Analysis.py
## 2.1 Overview of analysis.py
This file uses the functions outlined in [variablemodule.py](https://github.com/kknb1982/pands-project/blob/main/variablemodule.py) to create a text file of simple statistical analyses of the variables in Fisher's Iris Dataset, histograms of the single variables and scatter plots of variable pairs. To enable meaningful analysis the plots are coloured by the species of Iris.

## 2.2 The code
The code starts by importing all the required modules and data from the variablemodule file.
    
    from variablemodule import *

This first function creates a file and prints basic statistical information about each column to the file summary.txt(https://github.com/kknb1982/pands-project/blob/main/summary.txt).

    printfielddata()

The next function creates simple histograms without colouring and saves them as combinehist.png to the github repository.
    
    createsimplehist()

These histograms without colouring by species are hard to read and only show the overall spread of the data, it does not help to decide which variables actually allow identification of the species. Therefore, there is a further function `gethisto()` creates individual plots, coloured by species.

The next function creates scatter plot for the variable pairs and histograms for the univariate plots.

    createpairplot()

The next function creates box plots to graphically show most of the statistical data from the text file. The second function uses the subplot function to create the box plots [47]. 

    getboxplots()
    createboxsub()

The final function creates violinplots which shows the distribution of the data across the range.
    
    getviolinplots()

# 3. Variablemodule.py
## 3.1 Overview of variable module.py
## 3.2 The code
### 3.2.1 Import the libraries needed
In order to analyse the data a few libraries are needed:
* `Pandas` to import the dataset and create the dataframe [[1]](https://pandas.pydata.org/). 
* `Numpy` to create the statistical analyses of the data and support the creation of the plots [[2]](https://numpy.org/). 
* `Matplotlib` to create the simple histograms without colouring by species [[3]](https://matplotlib.org/). 
* `Seaborn` to create the coloured histograms and scatterplots [[4]](https://seaborn.pydata.org/index.html).

The libraries have been imported using aliases to make the code more streamlined. 

    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns 

### 3.2.2 Create the variable names
Fisher's Iris Dataset is published at https://archive.ics.uci.edu/ml/datasets/Iris/ [5](https://archive.ics.uci.edu/ml/datasets/Iris/). The data is published without variable names and therefore, these are created to be used in the dataframe and code.

    sepallen = "Sepal Length"
    sepalwid = "Sepal Width"
    petallen = "Petal Length"
    petalwid = "Petal Width"
    species = "Species"
    datafields = sepallen, sepalwid, petallen, petalwid, species

Due to the number of times the plotting functions need to call on the numerical columns of the data only a new variable has been created for this by slicing [[34]](https://www.geeksforgeeks.org/python-tuples/).

    chartvariables = datafields[:4]
    
### 3.2.3 Import Fishers Iris Dataset to a DataFrame
The code needs to import the Fisher's Iris Dataset and create a `DataFrame` using Pandas [[6]](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#csv-text-files).

    dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names = datafields)

### 3.2.4 Finds the names of the iris species
Throughout the analysis it is useful to interrogate the data and plot it for each species separately. The `Pandas` `unique()` method on the column "species" finds the unique values in this column [[7]](https://www.geeksforgeeks.org/get-unique-values-from-a-column-in-pandas-dataframe/). 

    irisspecies = dataf.Species.unique()

### 3.2.5 Defines a function to create a text file with summary data about the variable
The code now moves on to defining functions for the different analyses required [[8]](https://www.w3schools.com/python/python_functions.asp). First is the function `printfielddata`.

    def printfielddata():

Then a text file is opened to write the data to [[9]](https://www.geeksforgeeks.org/writing-to-file-in-python/). If the files does not exist the code will create it. 
    
    with open('summary.txt', 'w') as f:
    
There is then a `for` loop to iterate through the columns of the data [[10]](https://www.w3schools.com/python/python_for_loops.asp). An `if` statement [[11]](https://www.w3schools.com/python/python_conditions.asp) is used to ignore the "Species" column as this data is not numerical.
        
        for name in datafields:
            if name != species:
            
 The code then completes the following calculations for each of the variables:
 * Finds the minimum value [[12]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html)
 * Finds the maximum value [[13]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html)
 * Calculates the mean [[14]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)
 * Calculates the median [[15]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html)
 * Calculates the mode [[16]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html)

The calculated values as stored as strings [[17]](https://realpython.com/python-strings/) and written to the text file using `f.writelines`[[18]](https://www.pythontutorial.net/python-basics/python-write-text-file/). To get a neat layout `\n` is used to create new lines [[19]](https://www.w3schools.com/python/gloss_python_escape_characters.asp).  The data for each column or variable is separated by a header printed to the file using `f.write`. F strings [[20]](https://realpython.com/python-f-strings/) have been used to create the text for the file.


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
   
An `else` statement completes the analysis of the "Species" data [[11]](https://www.w3schools.com/python/python_conditions.asp). The data is separated by species [[21]](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html) and then `describe` used to analyse it [[22]](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.Series.describe.html#pandas.Series.describe). To write to the file the data needed to be in string format, 'to_string' is used for the conversion [[23]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html). 'header=True' and `index=True` ensures the header and row labels are printed. 
   
            else:
                for x in irisspecies:
                    f.writelines(f'\n{x} \n')
                    x = dataf[dataf["Species"] == x]
                    describex = x.describe()
                    stringx = describex.to_string(header=True, index =True)
                    f.writelines(stringx) 
                    
Once all the operations are complete the file is closed.

                f.close()
                
### 3.2.6 Create simple histograms
The next function `createsimplehist` uses the `matplotlib` histogram function to create a simple histogram of each of the variables of the dataset [[24]](https://matplotlib.org/stable/gallery/statistics/hist.html). `plt.savefig` is used to save the plot to the repository rather than outputting it to the terminal [[25]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig). The output is available in the file [combinedhist.png](https://github.com/kknb1982/pands-project/blob/main/combinedhist.png).

    def createsimplehist():
      dataf.hist()
      plt.savefig('combinedhist.png')
      plt.close()

### 3.2.7 Create histograms coloured by species
Without being able to visually separate the different species of iris in the histogram plots it is difficult to tell which, if any, variables offer discrimination. 
Seaborn was used [[4]](https://seaborn.pydata.org/) to create further histograms coloured by "species". A `for` loop creates each histogram in turn [[10]](https://www.w3schools.com/python/python_for_loops.asp).  Rather than using the `if name !=species` as used is 3.2.5 this function uses a different option, it slices the first four variables from the `datafields` tuple [[34]](https://www.geeksforgeeks.org/python-tuples/https://www.statology.org/pandas-subplots/). This can be simpler and enables the same variable name to be used throughout the scripts.

 and an `if` statement ensures graphs for all variables bar the species are created [[11](https://www.w3schools.com/python/python_conditions.asp).

    def gethisto():
      for name in chartvariables:
    
The histograms are created using Seaborn's `histplot` method with the following options [[26]](https://seaborn.pydata.org/generated/seaborn.histplot.html?highlight=histplot):
 * data source of the data as the dataframe, 
 * x- axis data as the variable being called in the `for` loop, 
 * hue (which colours the plot) by the species,
 * binwidth 0.1 to force the plot to have narrow columns, otherwise the automatically generated plot has different width bars across the species and measurements.
 
            sns.histplot(data=dataf, x=name, hue=species, binwidth=0.1)
        
This plot was then updated with an x-axis label [[27]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel) and title [[28]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html).
 
            plt.xlabel(f'{name} in cm')
            plt.title(f'Histogram of the relevant frequency of \n{name.lower()} highlighted by iris species')
            
The resulting figure was then saved and the plot closed.

            plt.savefig(name+ '.png')
            plt.close()

### 3.2.8 Create scatterplots
To create the scatterplots of the variable pairs the `pairplot` graph in Seaborn was used [[29]](https://seaborn.pydata.org/generated/seaborn.pairplot.html).  This easy to create graphic automatically plots each variable pair as a scatter plot and a layered Kernel Density Estimate (KDE) for the univariate plots. In order to create greater alignment with the earlier plots the option `diag_kind="hist"` was used to change this univariate plot to a histogram. To help the user understand the plots and increase their visual appeal `fig.suptitle`, `fig.supxlabel` and `fig.supylabel` were used [[30]](https://www.demo2s.com/python/python-matplotlib-plot-figure-labels-suptitle-supxlabel-supylabel.html). To create space for these super labels to show `fig.subplots_adjust` was used [[31]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html).

    def createpairplot():
      g= sns.pairplot(dataf, hue=species, diag_kind="hist")
      g.fig.subplots_adjust(left= .1, bottom=.1, top=.95)
      g.fig.suptitle('Pairplot of the variables in the Fisher Iris Dataset', fontsize = 16, fontweight='bold')
      g.fig.supxlabel('in cm')
      g.fig.supylabel('in cm')
      plt.savefig('pairplot.png')
      plt.close()
     
### 3.2.9 Create boxplots
Boxplots are very useful for giving a visual representation of the statistical information about some data. The Pandas Boxplot method was used to create the plots [[32]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html). The default figure sizing meant that the species labels overlapped making them unreadable, so it has been increased to 11 by 11. Savefig [[25]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig) was used to save a copy of this figure to the repository (https://github.com/kknb1982/pands-project/blob/main/boxplot.png). 

    def getboxplots():
       dataf.boxplot(by=species, figsize=(11,11))
       plt.savefig('boxplot.png')
       plt.close()
    
### 3.2.10 Creating boxplots using the subplot method
Using the method in 3.2.9 to create a box is quick, but it can be a little tricky to get the plot in exactly the format required. Therefore, this is an additional option using the subplot function [[33]](https://www.statology.org/pandas-subplots/). 
    
The first command in the funcation defines the core details about the subplots [[33]](https://www.statology.org/pandas-subplots/):

    def createboxsub():
      fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
      
This creates the sub-plots in a 2 by 2 grid [[33]](https://www.statology.org/pandas-subplots/) in the constrained layout [[35]](https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html) which automatically tries to layout the plots in a way where labels and titles do not overlap.

`suptitle` is used to create an overall title for the plot [[30]](https://www.demo2s.com/python/python-matplotlib-plot-figure-labels-suptitle-supxlabel-supylabel.html).

      plt.suptitle("Box plots of Fisher Iris Dataset by Species")

To ensure the subplots went to the correct axis a positional argument `a` is used. This is set to 1 at the start of the function and increases by after each subplot is created. This meant the first plot of data goes to subplot 1 and the second to subplot 2 and so on. 

The sub-plots were created with a `for` loop [[10]](https://www.w3schools.com/python/python_for_loops.asp). The subplots use Seaborn boxplot [[36]](https://seaborn.pydata.org/generated/seaborn.boxplot.html) `sns.boxplot` with the parameters to plot by species on the x axis and the current iterator on the y axis. Matplotlib's `ylabel` [[27]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) is used to create the y label. An `f string` [[20]](https://realpython.com/python-f-strings/) was used to format the y label. The positional variable was then increased by one to ensure the next set of data went to the next set of axes. 
      
      a = 1
      for name in chartvariables:
         plt.subplot(2,2,a)
         sns.boxplot(data=dataf, x=species, y=name)
         plt.ylabel(f'{name} in cm')
         a += 1
        
Once all the iterations were complete an `else` statement was used to create and save the plot [[25]].         
     
     else:
        plt.savefig('boxsub.png')
        
### 3.2.11 Create violinplots
A violin plot shows the distribution of data in a unique way [[37]](https://chartio.com/learn/charts/violin-plot-complete-guide/). A `for` loop was used to create each violinplot in turn [[10]](https://www.w3schools.com/python/python_for_loops.asp) and an `if` statement to ensure graphs for all variables bar the species were created [[11]](https://www.w3schools.com/python/python_conditions.asp).  Seaborn was used to create the violinplot [[38]](https://seaborn.pydata.org/generated/seaborn.violinplot.html). Defining the `x` parameter as species, splits the data by species in each of the plots. The plot readability was improved by adding a title [[28]] and ylabel [[27]].

    def getviolinplots():
     for name in datafields:
        if name != species:
            sns.violinplot(data=dataf, x=species, y=name)
            plt.ylabel(name+ 'in cm')
            plt.title(f'Violin plot of {name} in cm separated by species')
            plt.savefig(name+ 'violin.png')
            plt.close()
            
Using the structure in 3.2.11 these plots could be created as a single plot of subplots, rather than individually.

# 4. Further reading and information
For more information about the Iris Fisher Data Set, the code used in this file and using Python for visual data analyis please read [Descriptor.ipynb](https://github.com/kknb1982/pands-project/blob/main/Descriptor.ipynb). 

# 5. References
[1]: https://pandas.pydata.org/ "pandas - Python Data Analysis Library [Internet]. [cited 2023 May 10]". 

2. NumPy [Internet]. [cited 2023 May 4]. Available from: https://numpy.org/
3. Matplotlib — Visualization with Python [Internet]. [cited 2023 Apr 18]. Available from: https://matplotlib.org/
4. Waskom M. seaborn: statistical data visualization. J Open Source Softw. 2021 Apr 6;6(60):3021. 
5. UCI Machine Learning Repository: Iris Data Set [Internet]. [cited 2023 Apr 18]. Available from: https://archive.ics.uci.edu/ml/datasets/iris
6. IO tools (text, CSV, HDF5, …) — pandas 2.0.0 documentation [Internet]. [cited 2023 Apr 18]. Available from: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#csv-text-files
7. Get unique values from a column in Pandas DataFrame - GeeksforGeeks [Internet]. [cited 2023 May 8]. Available from: https://www.geeksforgeeks.org/get-unique-values-from-a-column-in-pandas-dataframe/
8. Python Functions [Internet]. [cited 2023 May 8]. Available from: https://www.w3schools.com/python/python_functions.asp
9. Writing to file in Python - GeeksforGeeks [Internet]. [cited 2023 May 8]. Available from: https://www.geeksforgeeks.org/writing-to-file-in-python/
10. Python For Loops [Internet]. [cited 2023 May 8]. Available from: https://www.w3schools.com/python/python_for_loops.asp
11. Python Conditions [Internet]. [cited 2023 May 8]. Available from: https://www.w3schools.com/python/python_conditions.asp
12. pandas.DataFrame.min — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html
13. pandas.DataFrame.max — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html
14. pandas.DataFrame.mean — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html
15. pandas.DataFrame.median — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.median.html
16. pandas.DataFrame.mode — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html
17. Strings and Character Data in Python – Real Python [Internet]. [cited 2023 May 8]. Available from: https://realpython.com/python-strings/
18. How to Write to Text File in Python [Internet]. [cited 2023 May 8]. Available from: https://www.pythontutorial.net/python-basics/python-write-text-file/
19. Python Escape Characters [Internet]. [cited 2023 May 8]. Available from: https://www.w3schools.com/python/gloss_python_escape_characters.asp
20. Python 3’s f-Strings: An Improved String Formatting Syntax (Guide) – Real Python [Internet]. [cited 2023 May 8]. Available from: https://realpython.com/python-f-strings/
21. How do I select a subset of a DataFrame? — pandas 2.0.0 documentation [Internet]. [cited 2023 Apr 22]. Available from: https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html
22. pandas.Series.describe — pandas 2.1.0.dev0+735.gf1126610ab documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.Series.describe.html#pandas.Series.describe
23. pandas.DataFrame.to_string — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html
24. Histograms — Matplotlib 3.7.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://matplotlib.org/stable/gallery/statistics/hist.html
25. matplotlib.pyplot.savefig — Matplotlib 3.7.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig
26. seaborn.histplot — seaborn 0.12.2 documentation [Internet]. [cited 2023 May 8]. Available from: https://seaborn.pydata.org/generated/seaborn.histplot.html?highlight=histplot
27. matplotlib.pyplot.xlabel — Matplotlib 3.7.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
28. matplotlib.pyplot.title — Matplotlib 3.7.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
29. seaborn.pairplot — seaborn 0.12.2 documentation [Internet]. [cited 2023 Apr 22]. Available from: https://seaborn.pydata.org/generated/seaborn.pairplot.html
30. Python matplotlib plot Figure labels: suptitle, supxlabel, supylabel [Internet]. [cited 2023 May 11]. Available from: https://www.demo2s.com/python/python-matplotlib-plot-figure-labels-suptitle-supxlabel-supylabel.html
31. matplotlib.pyplot.subplots_adjust — Matplotlib 3.7.1 documentation [Internet]. [cited 2023 May 11]. Available from: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
32. pandas.DataFrame.boxplot — pandas 2.0.1 documentation [Internet]. [cited 2023 May 8]. Available from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
33. Pandas: How to Plot Multiple DataFrames in Subplots - Statology [Internet]. [cited 2023 May 11]. Available from: https://www.statology.org/pandas-subplots/
34. Python Tuples - GeeksforGeeks [Internet]. [cited 2023 May 11]. Available from: https://www.geeksforgeeks.org/python-tuples/
35. Constrained Layout Guide — Matplotlib 3.7.1 documentation [Internet]. [cited 2023 May 11]. Available from: https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html
36. Seaborn.boxplot — seaborn 0.12.2 documentation [Internet]. [cited 2023 May 11]. Available from: https://seaborn.pydata.org/generated/seaborn.boxplot.html
37. seaborn.violinplot — seaborn 0.12.2 documentation [Internet]. [cited 2023 May 9]. Available from: https://seaborn.pydata.org/generated/seaborn.violinplot.html
38. A Complete Guide to Violin Plots | Tutorial by Chartio [Internet]. [cited 2023 May 9]. Available from: https://chartio.com/learn/charts/violin-plot-complete-guide/
