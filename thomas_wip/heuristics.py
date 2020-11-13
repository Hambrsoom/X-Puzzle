from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation
import numpy as np

def h0(puzzleArray, xDim, yDim):
    if puzzleArray[-1] == '0':
        return 0
    else:
        return 1

#Hamming distance
def h1(puzzleArray, xDim, yDim):
    elementShouldEqualTo = 1
    hn = 0
    for element in puzzleArray:
        if int(element) != elementShouldEqualTo or (int(element) == int(puzzleArray[-1]) and int(element) != 0):
            hn = hn + 1
        elementShouldEqualTo = elementShouldEqualTo + 1
    return hn 

# # Manhattan
# def manhattanHeuristic(puzzleArray, nRows, nColumns):
#     index = 0
#     hn = 0
#     for element in puzzleArray:
        
#         if 
#         else:


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

