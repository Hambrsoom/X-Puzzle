from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation
import numpy as np

#Hamming distance
def h1(puzzleArray, xDim, yDim):
    elementShouldEqualTo = 1
    hn = 0
    for element in puzzleArray:
        if int(element) != elementShouldEqualTo or (int(element) == int(puzzleArray[-1]) and int(element) != 0):
            hn = hn + 1
        elementShouldEqualTo = elementShouldEqualTo + 1
    return hn 

# Manhattan
def h2(puzzleArray, nRows, nColumns):
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

#sumOfPermutationInversions
def h3(puzzleArray, xDim, yDim):
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
    # return checkGoal1