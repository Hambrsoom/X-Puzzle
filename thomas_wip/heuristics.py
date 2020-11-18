from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation
import numpy as np

# Hamming distance
def hammingDistance(puzzleArray, xDim, yDim, firstSolutionList, secondSolutionList):
    elementShouldEqualTo = 1
    hn1 = 0
    hn2 = 0
    # Find how many elements of the puzzleArray are not in their right position according to the first solution
    # [[1 2 3 4],
    #  [5 6 7 0]]
    for element in puzzleArray:
        if int(element) != elementShouldEqualTo or (int(element) == int(puzzleArray[-1]) and int(element) != 0):
            hn1 = hn1 + 1
        elementShouldEqualTo = elementShouldEqualTo + 1
    
    # Find how many elements of the puzzleArray are not in their right position according to the first solution
    # [[1 3 5 7],
    #  [2 4 6 0]]
    for i in range(len(puzzleArray)):
        if int(puzzleArray[i]) != int(secondSolutionList[i]):
            hn2 = hn2 + 1 
    return min(hn1, hn2) 

# Manhattan
def manhattan(puzzleArray, nRows, nColumns, firstSolutionList, secondSolutionList):

    # Reshaping the solutions the puzzle to be like a 2d array.
    chunksProperListFirstSolution = np.array(firstSolutionList).reshape(nColumns, nRows)
    chunksProperListSecondSolution = np.array(secondSolutionList).reshape(nColumns, nRows)
    chunksPuzzleList = np.array(puzzleArray).reshape(nColumns, nRows)
    firstTotalDistance = 0
    secondTotalDistance = 0

    for y in range(len(chunksPuzzleList)):
        for x in range(len(chunksPuzzleList[y])):
            # Finding the proper location of each x and y according to solution one.
            properLocationYFirstSolution, properLocationXFirstSolution = properLocationOfNode(chunksPuzzleList[y][x], chunksProperListFirstSolution)
            
            # Finding the proper location of each x and y according to solution two.
            properLocationYSecondSolution, properLocationXSecondSolution = properLocationOfNode(chunksPuzzleList[y][x], chunksProperListSecondSolution)
            
            # Calculating the total distance of moving the elements to their proper place according to solution one & solution two
            firstTotalDistance = firstTotalDistance + calculateDistance(properLocationXFirstSolution, properLocationYFirstSolution, y, x)
            secondTotalDistance = secondTotalDistance + calculateDistance(properLocationXSecondSolution, properLocationYSecondSolution, y, x)
    return min(firstTotalDistance, secondTotalDistance)

# find the location of a node in a list.
def properLocationOfNode(node, list):
    for y in range(len(list)):
        for x in range(len(list[y])):
            if list[y][x] == int(node):
                return y, x


# Calucate the distance on both x and y access separately and then take their sum
def calculateDistance(properX, properY, realX, realY):
    return abs(properX-realX) + abs(properY - realY)

