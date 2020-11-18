import csv
import random
from helper_methods import listToString


# import the puzzles from a txt file
def importPuzzlesFromFile(filePath):
    with open(filePath, newline='') as file:
        reader = csv.reader(file, delimiter=' ')
        res = list(reader)
        return res

# generate a txt file which has a puzzle on each line according to the number of rows and columns requested
def generateFileOfFiftyPuzzles(nRows, nColumns, nPuzzles):
    list = []
    file = open("puzzles.txt", "w")    
    
    for number in range(nRows*nColumns):
        list.append(number)

    for number in range(nPuzzles):
        random.shuffle(list)
        file.write(listToString(list) + "\n")

    file.close()
