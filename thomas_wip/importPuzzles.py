import csv

def importPuzzlesFromFile(filePath):
    with open(filePath, newline='') as file:
        reader = csv.reader(file, delimiter=' ')
        res = list(reader)
        return res