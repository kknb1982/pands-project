import pandas as pd 
#

sepallen = "Sepal Length"
sepalwid = "Sepal Width"
petallen = "Petal Length"
petalwid = "Petal Width"
species = "Species"

datafields = sepallen, sepalwid, petallen, petalwid, species

# Import data
dataf = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                   names = datafields)

def printfielddata():
    with open('summary.txt', 'a') as f:
        for name in datafields:
            if name != species:
                header = (f'The column title is {name}')
                f.write(header)
                min = str(data[name].min())
                max = str(data[name].max())
                range = (f'\nThe minimum values is: {min} \nThe maximum value is: {max}')
                f.writelines(range)
                mean = str(data[name].mean())
                median = str(data[name].median())
                mode = str(data[name].mode())
                averages = (f'\nMean: {mean} \nMedian: {median} \nMode: {mode}\n\n')
                f.writelines(averages)
            else:
                f.close()