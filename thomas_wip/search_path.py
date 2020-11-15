from pprint import pprint
from helper_methods import listToString

def getSearchPath(closedArr, algoType, puzzleNumber, foundSolution):
    print("Search Path")
    
    fileName = "output/" + str(puzzleNumber) + "_" + algoType + "_search" +".txt"

    file = open(fileName, "w")

    if foundSolution:
        for node in reversed(closedArr):
            if algoType == "ucs":
                gn = node["gn"]
                hn = 0
                fn = 0
            elif algoType == "gbfs":
                gn = 0
                hn = node["hn"]
                fn = 0
            elif algoType == "astar":
                gn = node["gn"]
                hn = node["hn"]
                fn = node["fn"]
            currentState = node["currentState"]

            file.write(str(fn) + " " + str(gn) + " " + str(hn) + " " + listToString(currentState) + "\n")
    else:
        file.write("no solution")
    
    file.close()
