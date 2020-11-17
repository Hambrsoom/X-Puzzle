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
    chunksProperListFirstSolution = [firstSolutionList[x:x+nColumns] for x in range(0, len(firstSolutionList), nColumns)]
    chunksProperListSecondSolution = [secondSolutionList[x:x+nColumns] for x in range(0, len(secondSolutionList), nColumns)]

    chunksPuzzleList = [puzzleArray[x:x+nColumns] for x in range(0, len(puzzleArray), nColumns)]
    totalCost = 0

    for i in range(len(chunksPuzzleList)):
        for j in range(len(chunksPuzzleList[i])):
            properLocationXFirstSolution, porperLocationYFirstSolution = properLocationOfNode(chunksPuzzleList[i][j], chunksProperListFirstSolution)
            properLocationXSecondSolution, porperLocationYSecondSolution = properLocationOfNode(chunksPuzzleList[i][j], chunksProperListSecondSolution)

            totalCost = totalCost + min(calculateCost(properLocationXFirstSolution, porperLocationYFirstSolution, i, j),  calculateCost(properLocationXSecondSolution, porperLocationYSecondSolution, i, j))
    return totalCost

def properLocationOfNode(node, list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == int(node):
                return i, j

def calculateCost(properX, properY, realX, realY):
    return abs(properX-realX) + abs(properY - realY)


#sumOfPermutationInversions
def h3(puzzleArray, xDim, yDim, firstSolutionList, secondSolutionList):
    arrCopy = puzzleArray.copy();
    indexOf0 = arrCopy.index('0');
    arrCopy[indexOf0] = len(arrCopy); #change 0 to length of puzzle in order to allow Permutation.inversions()
    arrCopy = np.hstack((0,arrCopy));
    checkGoal1 = Permutation(arrCopy).inversions();
    arrCopy = arrCopy[1:];
    splitArr = np.array_split(arrCopy, yDim);
    arrVertical = [0] * len(arrCopy);
    count = 0;
    for arr in splitArr:
        for i in arr:
            arrVertical[count] = i;
            count = count + yDim;
        count = 1;
    arrVertical = np.hstack((0,arrVertical));
    return min(checkGoal1, Permutation(arrVertical).inversions());
