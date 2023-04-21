from variablemodule import *

def getfielddata():
    for name in datafields:
        if name != species:
            print (name)
            min = data[name].min()
            max = data[name].max()
            print("Minimum: ", min, "\nMaximum: ", max)
            mean = data[name].mean()
            median = data[name].median()
            mode = data[name].mode()
            print("Mean: ", mean,"\nMedian: ", median, "\nMode: ", mode)
            name = data[[name, species]]
     
        else: 
            break