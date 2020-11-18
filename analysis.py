import csv
import os
import fnmatch

ucsSolution = 0
ucsSearch = 0
ucsNoSolution = 0
ucsTime = 0
ucsCost = 0

gbfsh1Search = 0
gbfsh2Search = 0
gbfsh1Solution = 0
gbfsh2Solution = 0
gbfsh1Time = 0
gbfsh2Time = 0
gbfsh1Cost = 0
gbfsh2Cost = 0
gbfsh1NoSolution = 0
gbfsh2NoSolution = 0

aStarh1Search = 0
aStarh2Search = 0
aStarh1Solution = 0
aStarh2Solution = 0
aStarh1Time = 0
aStarh2Time = 0
aStarh1Cost = 0
aStarh2Cost = 0
aStarh1NoSolution = 0
aStarh2NoSolution = 0
def getLineCount(filename):
    temp = filename
    filename = ".\\output\\" + temp
    return sum(1 for line in open(filename))

def getLastLine(filename):
    temp = filename
    filename = ".\\output\\" + temp
    with open(filename) as f:
        for line in f:
            pass
        last_line = line
    return last_line

def getFirstLine(filename):
    temp = filename
    filename = ".\\output\\" + temp
    with open(filename) as f:
        return f.readline()

def writeInfoOnFile(file, totalNumberLine, averageNumberLine, calcutedNumber):
    file.write(totalNumberLine + str(calcutedNumber))
    file.write("\n")
    file.write(averageNumberLine + str(calcutedNumber/50))
    file.write("\n\n")

def generateTheListOfLowestCost():
    dic = {
        0: 16,
        1: 11,
        2: 12,
        3: 14,
        4: "no solution",
        5: 12,
        6: 13,
        7: 15,
        8: 12,
        9: 14,
        10: 12,
        11: 14,
        12: 12,
        13: "no solution",
        14: 17,
        15: 15,
        16: 12,
        17: 12,
        18: 10,
        19: 15,
        20: 13,
        21: 13,
        22: "no solution",
        23: 14,
        24: 17,
        25: 17,
        26: "no solution",
        27: 14,
        28: 13,
        29: 15,
        30: 12,
        31: 16,
        32: 12,
        33: 15,
        34: 11,
        35: 12,
        36: 17,
        37: 17,
        38: 12,
        39: 16,
        40: "no solution",
        41: 15,
        42: 16,
        43: 14,
        44: 12,
        45: 17,
        46: 13,
        47: 14,
        48: 16,
        49: 13,
    }
    return dic

dictOfLowestCostForPuzzles = generateTheListOfLowestCost()
dictOfAlgoOptimalitySolutionPath = {
    "gbfs-h1": 0,
    "gbfs-h2": 0,
    "astar-h1": 0,
    "astar-h2": 0,
    "ucs": 0
}
dictOfAlgoFindingTheLowestCostPath = {}

def checkIfCostOfAlgoIsLowestCostPath(cost, puzzleNumber, dictOfLowestCostForPuzzles):
    print(puzzleNumber)
    lowestCost = dictOfLowestCostForPuzzles[puzzleNumber]
    if lowestCost != "no solution":
        return lowestCost == cost
    else:
        return False

for filename in os.listdir("output"):
    # GBFS:
    if "gbfs-h1_search" in filename:
        gbfsh1Search = gbfsh1Search + getLineCount(filename)
    elif "gbfs-h2_search" in filename:
        gbfsh2Search = gbfsh2Search + getLineCount(filename)

    elif "gbfs-h1_solution" in filename:
        if(getFirstLine(filename) == "no solution"):
            gbfsh1NoSolution = gbfsh1NoSolution + 1
        else:
            gbfsh1Solution = gbfsh1Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            gbfsh1Cost = gbfsh1Cost + int(lastLine[0])
            gbfsh1Time = gbfsh1Time + float(lastLine[1])
            puzzleNumber = int(filename.split("_")[0])
            if checkIfCostOfAlgoIsLowestCostPath(int(lastLine[0]), puzzleNumber, dictOfLowestCostForPuzzles):
                dictOfAlgoOptimalitySolutionPath["gbfs-h1"] = dictOfAlgoOptimalitySolutionPath["gbfs-h1"] + 1
                if puzzleNumber in dictOfAlgoFindingTheLowestCostPath:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("gbfs-h1")
                else:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber] = []
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("gbfs-h1")


    elif "gbfs-h2_solution" in filename:
        if(getFirstLine(filename) == "no solution"):
            gbfsh2NoSolution = gbfsh2NoSolution + 1
        else:
            gbfsh2Solution = gbfsh2Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            gbfsh2Cost = gbfsh2Cost + int(lastLine[0])
            gbfsh2Time = gbfsh2Time + float(lastLine[1])
            puzzleNumber = int(filename.split("_")[0])
            if checkIfCostOfAlgoIsLowestCostPath(int(lastLine[0]), puzzleNumber, dictOfLowestCostForPuzzles):
                dictOfAlgoOptimalitySolutionPath["gbfs-h2"] = dictOfAlgoOptimalitySolutionPath["gbfs-h2"] + 1
                if puzzleNumber in dictOfAlgoFindingTheLowestCostPath:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("gbfs-h2")
                else:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber] = []
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("gbfs-h2")
    
    # A* star
    elif "astar-h1_search" in filename:
        aStarh1Search = aStarh1Search + getLineCount(filename)

    elif "astar-h2_search" in filename:
        aStarh2Search = aStarh2Search + getLineCount(filename)
    elif "astar-h1_solution" in filename:
        if(getFirstLine(filename) == "no solution"):
            aStarh1NoSolution = aStarh1NoSolution + 1
        else:
            aStarh1Solution = aStarh1Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            aStarh1Cost = aStarh1Cost + int(lastLine[0])
            aStarh1Time = aStarh1Time + float(lastLine[1])
            puzzleNumber = int(filename.split("_")[0])
            if checkIfCostOfAlgoIsLowestCostPath(int(lastLine[0]), puzzleNumber, dictOfLowestCostForPuzzles):
                dictOfAlgoOptimalitySolutionPath["astar-h1"] = dictOfAlgoOptimalitySolutionPath["astar-h1"] + 1
                if puzzleNumber in dictOfAlgoFindingTheLowestCostPath:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("astar-h1")
                else:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber] = []
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("astar-h1")

    elif "astar-h2_solution" in filename:
        if(getFirstLine(filename) == "no solution"):
            aStarh2NoSolution = aStarh2NoSolution + 1
        else:
            aStarh2Solution = aStarh2Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            aStarh2Cost = aStarh2Cost + int(lastLine[0])
            aStarh2Time = aStarh2Time + float(lastLine[1])
            puzzleNumber = int(filename.split("_")[0])
            if checkIfCostOfAlgoIsLowestCostPath(int(lastLine[0]), puzzleNumber, dictOfLowestCostForPuzzles):
                dictOfAlgoOptimalitySolutionPath["astar-h2"] = dictOfAlgoOptimalitySolutionPath["astar-h2"] + 1
                if puzzleNumber in dictOfAlgoFindingTheLowestCostPath:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("astar-h2")
                else:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber] = []
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("astar-h2")


    # elif fnmatch.fnmatch(filename, 'ucs') and fnmatch.fnmatch(filename, 'search'):
    elif "ucs_search" in filename:
        ucsSearch = ucsSearch + getLineCount(filename)
    elif "ucs_solution" in filename:
        if(getFirstLine(filename) == "no solution"):
            ucsNoSolution = ucsNoSolution + 1
        else:
            ucsSolution = ucsSolution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            ucsCost = ucsCost + int(lastLine[0])
            ucsTime = ucsTime + float(lastLine[1])
            puzzleNumber = int(filename.split("_")[0])
            if checkIfCostOfAlgoIsLowestCostPath(int(lastLine[0]), puzzleNumber, dictOfLowestCostForPuzzles):
                dictOfAlgoOptimalitySolutionPath["ucs"] = dictOfAlgoOptimalitySolutionPath["ucs"] + 1
                if puzzleNumber in dictOfAlgoFindingTheLowestCostPath:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("ucs")
                else:
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber] = []
                    dictOfAlgoFindingTheLowestCostPath[puzzleNumber].append("ucs")

file = open("analysisResults.txt", "w")

# 1. average & total length of the solution and search paths

# ucs solution path
file.write("average & total length of the solution paths \n\n")

writeInfoOnFile(file, "Total ucs solution path: ", "Average ucs solution path: ", ucsSolution)
writeInfoOnFile(file, "Total gbfs-h1 solution path: ", "Average gbfs-h1 solution path: ", gbfsh1Solution)
writeInfoOnFile(file, "Total gbfs-h2 solution path: ", "Average gbfs-h2 solution path: ", gbfsh2Solution)
writeInfoOnFile(file, "Total astar-h1 solution path: ", "Average astar-h1 solution path: ", aStarh1Solution)
writeInfoOnFile(file, "Total astar-h2 solution path: ", "Average astar-h2 solution path: ", aStarh2Solution)

# ucs search path
file.write("average & total length of the search paths: \n\n")

writeInfoOnFile(file, "Total ucs search path: ", "Average ucs search path: ", ucsSearch)
writeInfoOnFile(file, "Total gbfs-h1 search path: ", "Average gbfs-h1 search path: ", gbfsh1Search)
writeInfoOnFile(file, "Total gbfs-h2 search path: ", "Average gbfs-h2 search path: ", gbfsh2Search)
writeInfoOnFile(file, "Total astar-h1 search path: ", "Average astar-h1 search path: ", aStarh1Search)
writeInfoOnFile(file, "Total astar-h2 search path: ", "Average astar-h2 search path: ", aStarh2Search)

# 2. average & total number of no solution,
# ucs no solution path
file.write("average & total number of no solution: \n\n")

writeInfoOnFile(file, "Total number of no solution with ucs: ", "Average number of no solution with ucs: ", ucsNoSolution)
writeInfoOnFile(file, "Total number of no solution with gbfs-h1: ", "Average number of no solution with gbfs-h1: ", gbfsh1NoSolution)
writeInfoOnFile(file, "Total number of no solution with gbfs-h2: ", "Average number of no solution with gbfs-h2: ", gbfsh2NoSolution)
writeInfoOnFile(file, "Total number of no solution with astar-h1: ", "Average number of no solution with astar-h1: ", aStarh1NoSolution)
writeInfoOnFile(file, "Total number of no solution with astar-h2: ", "Average number of no solution with astar-h2: ", aStarh2NoSolution)

# 3. average & total cost and execution time

# ucs cost
file.write("average & total cost: \n\n")
writeInfoOnFile(file, "Total cost of ucs: ", "Average cost of ucs: ", ucsCost)
writeInfoOnFile(file, "Total cost of gbfs-h1: ", "Average cost of gbfs-h1: ", gbfsh1Cost)
writeInfoOnFile(file, "Total cost of with gbfs-h2: ", "Average cost of gbfs-h2: ", gbfsh2Cost)
writeInfoOnFile(file, "Total cost of astar-h1: ", "Average cost of astar-h1: ", aStarh1Cost)
writeInfoOnFile(file, "Total cost of astar-h2: ", "Average cost of astar-h2: ", aStarh2Cost)

# ucsCost
file.write("average & total execution time: \n\n")
writeInfoOnFile(file, "Total execution time of ucs: ", "Average execution time of ucs: ", ucsTime)
writeInfoOnFile(file, "Total execution time of gbfs-h1: ", "Average execution time of gbfs-h1: ", gbfsh1Time)
writeInfoOnFile(file, "Total execution time of with gbfs-h2: ", "Average execution time of gbfs-h2: ", gbfsh2Time)
writeInfoOnFile(file, "Total execution time of astar-h1: ", "Average execution time of astar-h1: ", aStarh1Time)
writeInfoOnFile(file, "Total execution time of astar-h2: ", "Average execution time of astar-h2: ", aStarh2Time)

# 4. optimality of the solution path
file.write("optimality of the solution path: \n\n")
for key, value in dictOfAlgoFindingTheLowestCostPath.items():
    file.write("Puzzle " + str(key) + ": " )
    for element in value:
        if(element != value[-1]):
            file.write(element + " -- ")
        else:
            file.write(element)
    file.write("\n")

file.write("\n\n")
file.write("Summary of how many each alogrithm got the lowest cost \n\n")
for key, value in dictOfAlgoOptimalitySolutionPath.items():
    file.write(key + ": " + str(value) + "\n")
    

file.close()
