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
gbfsth2Solution = 0
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



for filename in os.listdir("output"):
    if fnmatch.fnmatch(filename, 'gbfs-h1') and fnmatch.fnmatch(filename, 'search'):
        gbfsh1Search = gbfsh1Search + getLineCount(filename)
    elif fnmatch.fnmatch(filename, 'gbfs-h2') and fnmatch.fnmatch(filename, 'search'):
        gbfsh2Search = gbfsh2Search + getLineCount(filename)
    elif fnmatch.fnmatch(filename, 'gbfs-h1') and fnmatch.fnmatch(filename, 'solution'):
        if(getFirstLine(filename) == "no solution"):
            gbfsh1NoSolution = gbfsh1NoSolution + 1
        else:
            gbfsh1Solution = gbfsh1Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            gbfsh1Cost = gbfsh1Cost + lastLine[0]
            gbfsh1Time = gbfsh1Time + lastLine[1]
    elif fnmatch.fnmatch(filename, 'gbfs-h2') and fnmatch.fnmatch(filename, 'solution'):
        if(getFirstLine(filename) == "no solution"):
            gbfsh2NoSolution = gbfsh2NoSolution + 1
        else:
            agbfsh2Solution = agbfsh2Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            gbfsh2Cost = gbfsh2Cost + lastLine[0]
            gbfsh2Time = gbfsh2Time + lastLine[1]

    elif fnmatch.fnmatch(filename, 'astar-h1') and fnmatch.fnmatch(filename, 'search'):
        Astarh1Search = Astarh1Search + getLineCount(filename)
    elif fnmatch.fnmatch(filename, 'astar-h2') and fnmatch.fnmatch(filename, 'search'):
        Astarh2Search = Astarh2Search + getLineCount(filename)
    elif fnmatch.fnmatch(filename, 'astar-h1') and fnmatch.fnmatch(filename, 'solution'):
        if(getFirstLine(filename) == "no solution"):
            aStarh1NoSolution = aStarh1NoSolution + 1
        else:
            aStarh1Solution = aStarh1Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            aStarh1Cost = aStarh1Cost + lastLine[0]
            aStarh1Time = aStarh1Time + lastLine[1]
    elif fnmatch.fnmatch(filename, 'astar-h2') and fnmatch.fnmatch(filename, 'solution'):
        if(getFirstLine(filename) == "no solution"):
            aStarh2NoSolution = aStarh2NoSolution + 1
        else:
            aStarh2Solution = aStarh2Solution + (getLineCount(filename) - 1)
            lastLine = getLastLine(filename).split()
            aStarh2Cost = aStarh2Cost + lastLine[0]
            aStarh2Time = aStarh2Time + lastLine[1]

    elif fnmatch.fnmatch(filename, 'ucs') and fnmatch.fnmatch(filename, 'search'):
        ucsSearch = ucsSearch + getLineCount(filename)
    elif fnmatch.fnmatch(filename, 'ucs') and fnmatch.fnmatch(filename, 'solution'):
        ucsSolution = ucsSolution + (getLineCount(filename) - 1)
        lastLine = getLastLine(filename).split()
        ucsCost = ucsCost + lastLine[0]
        ucsTime = ucsTime + lastLine[1]



file = open("analysisResults.txt", "w")


file.write("UNIFORM COST\n")
file.write("-----------------------------\n\n")

##TODO: output all stats

file.close()

def getLineCount(fileName):
    return sum(1 for line in open(fileName))

def getLastLine(filename):
    with open(filename) as f:
        for line in f:
            pass
        last_line = line
    return last_line

def getFirstLine(fileName):
    with open(fileName) as f:
        return f.readline()
