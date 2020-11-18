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

def isDecreasing(puzzleArray, nRows, nColumns, firstSolutionList, secondSolutionList):
    arrCopy = puzzleArray.copy()
    
    # convert to int
    for idx, val in enumerate(arrCopy): arrCopy[idx] = int(arrCopy[idx])

    indexOf0 = arrCopy.index(0)
    arrCopy[indexOf0] = len(arrCopy)

    # Reshaping the solutions the puzzle to be like a 2d array.
    chunksPuzzleList = np.array(arrCopy).reshape(nColumns, nRows)
    seenDecrease = 0

    for y in range(len(chunksPuzzleList)):
        rowSorted = np.all(np.diff(chunksPuzzleList[y]) >= 0)
        if not rowSorted: 
            seenDecrease = seenDecrease + 1
    
    return seenDecrease
