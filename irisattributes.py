def getdatainformation(data):
    for name in datafields:
        print ("The data field name is: "name")
        print (data[name].mean())
        print (data[name].min())
        print (data[name].max())
        print (data[name].median())
        print (" ")