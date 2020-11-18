from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation
import numpy as np

#Hamming distance
def hammingDistance(puzzleArray, xDim, yDim, firstSolutionList, secondSolutionList):
    elementShouldEqualTo = 1
    hn1 = 0
    hn2 = 0
    for element in puzzleArray:
        if int(element) != elementShouldEqualTo or (int(element) == int(puzzleArray[-1]) and int(element) != 0):
            hn1 = hn1 + 1
        elementShouldEqualTo = elementShouldEqualTo + 1
    
    for i in range(len(puzzleArray)):
        if int(puzzleArray[i]) != int(secondSolutionList[i]):
            hn2 = hn2 + 1 
    return min(hn1, hn2) 

# Manhattan
def manhattan(puzzleArray, nRows, nColumns, firstSolutionList, secondSolutionList):
    chunksProperListFirstSolution = np.array(firstSolutionList).reshape(nColumns, nRows)
    chunksProperListSecondSolution = np.array(secondSolutionList).reshape(nColumns, nRows)
    chunksPuzzleList = np.array(puzzleArray).reshape(nColumns, nRows)
    firstTotalDistance = 0
    secondTotalDistance = 0

    for y in range(len(chunksPuzzleList)):
        for x in range(len(chunksPuzzleList[y])):
            properLocationYFirstSolution, properLocationXFirstSolution = properLocationOfNode(chunksPuzzleList[y][x], chunksProperListFirstSolution)
            properLocationYSecondSolution, properLocationXSecondSolution = properLocationOfNode(chunksPuzzleList[y][x], chunksProperListSecondSolution)
            firstTotalDistance = firstTotalDistance + calculateDistance(properLocationXFirstSolution, properLocationYFirstSolution, y, x)
            secondTotalDistance = secondTotalDistance + calculateDistance(properLocationXSecondSolution, properLocationYSecondSolution, y, x)
    return min(firstTotalDistance, secondTotalDistance)

def properLocationOfNode(node, list):
    for y in range(len(list)):
        for x in range(len(list[y])):
            if list[y][x] == int(node):
                return y, x

def calculateDistance(properX, properY, realX, realY):
    return abs(properX-realX) + abs(properY - realY)

