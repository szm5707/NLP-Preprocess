import os

currentDirectoryPath = os.getcwd()
dataSetPath = currentDirectoryPath + "/dataset"
allFiles = os.listdir(dataSetPath)



for file in allFiles:
    if(".xml" in file):
        filename = "dataset/" + file
        print(filename)
        fo = open(filename, 'r')
        lines = fo.readlines()
        newlines = []
        for line in lines:
            if line[:8] == "<seg id=":
                newlines.append(line[13:-8])

        OutputFileName = "dataset/Output/Stripped-" + file[:-3] +"txt"
        print(OutputFileName)
        f = open(OutputFileName,"w+")

        for line in newlines:
            f.write(line + "\n")
