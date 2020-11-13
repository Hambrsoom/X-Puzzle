#Hamming distance
def hammingDistanceHeuristic(puzzleArray, nRows, nColumns):
    elementShouldEqualTo = 1
    hn = 0
    for element in puzzleArray:
        if int(element) != elementShouldEqualTo or (int(element) == int(puzzleArray[-1]) and int(element) != 0):
            hn = hn + 1
        elementShouldEqualTo = elementShouldEqualTo + 1
    return hn 

# # Manhattan
def manhattanHeuristic(puzzleArray, nRows, nColumns):
    properList = []
    for number in range(len(puzzleArray)):
        properList.append(number+1)

    properList[-1] = 0
    chunksProperList = [properList[x:x+nColumns] for x in range(0, len(properList), nColumns)]
    chunksPuzzleList = [puzzleArray[x:x+nColumns] for x in range(0, len(puzzleArray), nColumns)]
    totalCost = 0

    for i in range(len(chunksPuzzleList)):
        for j in range(len(chunksPuzzleList[i])):
            properLocationX, porperLocationY = properLocationOfNode(chunksPuzzleList[i][j], chunksProperList)
            totalCost = totalCost + calculateCost(properLocationX, porperLocationY, i, j)
    return totalCost

def properLocationOfNode(node, list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == int(node):
                return i, j

def calculateCost(properX, properY, realX, realY):
    return abs(properX-realX) + abs(properY - realY)

# def generateSecondSolution(nRows, nColumns):
#     for number in ra
