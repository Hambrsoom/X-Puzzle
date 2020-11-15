import csv
import random
from helper_methods import listToString

def importPuzzlesFromFile(filePath):
    with open(filePath, newline='') as file:
        reader = csv.reader(file, delimiter=' ')
        res = list(reader)
        return res


def generateFileOfFiftyPuzzles(nRows, nColumns, nPuzzles):
    list = []

    file = open("puzzles.txt", "w")    
    
    for number in range(nRows*nColumns):
        list.append(number)

    for number in range(nPuzzles):
        random.shuffle(list)
        file.write(listToString(list) + "\n")

    file.close()
