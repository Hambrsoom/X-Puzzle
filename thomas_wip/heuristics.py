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
    firstTotalCost = 0
    secondTotalCost = 0

    for row in range(len(chunksPuzzleList)):
        print("row=======================", chunksPuzzleList[row])
        for column in range(len(chunksPuzzleList[row])):
            print("column=======================", chunksPuzzleList[row][column])
            properLocationXFirstSolution, porperLocationYFirstSolution = properLocationOfNode(chunksPuzzleList[row][column], chunksProperListFirstSolution)
            properLocationXSecondSolution, porperLocationYSecondSolution = properLocationOfNode(chunksPuzzleList[row][column], chunksProperListSecondSolution)
            firstTotalCost = firstTotalCost + calculateCost(properLocationXFirstSolution, porperLocationYFirstSolution, row, column, nRows, nColumns)
            secondTotalCost = secondTotalCost + calculateCost(properLocationXSecondSolution, porperLocationYSecondSolution, row, column, nRows, nColumns)
    print("===================================", min(firstTotalCost, secondTotalCost))
    return min(firstTotalCost, secondTotalCost)

def properLocationOfNode(node, list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == int(node):
                return i, j

def calculateCost(properX, properY, realX, realY, nRows, nColumns):
    print("properX  ================", properX)
    print("properY =================", properY)

    # Vertical and horizontal wrapping
    if realX == properX and ((realY == 0 and properY == nColumns-1) or (realY == nColumns-1 and properY == 0)):
        return 1
    if realY == properY and ((realX == 0 and properX == nRows-1)) or (realX == nRows-1 and properX == 0):
        return 1
    

    # Diagonal
    if abs(realX - properX) == 1 and abs(realY - properY) == 1:
        return 1

    # opposite Diagnoals move
    if (realX == 0 and realY == 0) and (properX == nRows-1 and properY ==  nColumns-1):
        return 1
    if (realX == nRows-1 and realY ==  nColumns-1) and (properX == 0 and properY == 0):
        return 1
    if (realX == 0 and realY == nColumns-1) and (properX == nRows-1 and properY == 0):
        return 1
    if (realX == nRows-1 and realY == 0) and (properX == 0 and properY == nColumns-1):
        return 1

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
    splitCount = 0;
    for arr in splitArr:
        count = splitCount
        for i in arr:
            arrVertical[count] = i;
            count = count + yDim;
        splitCount = splitCount + 1;
    arrVertical = np.hstack((0,arrVertical));
    return min(checkGoal1, Permutation(arrVertical).inversions());
