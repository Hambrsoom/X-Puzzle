def h0(puzzleArray):
    if puzzleArray[-1] == '0':
        return 0
    else:
        return 1

#Hamming distance
def hammingDistanceHeuristic(puzzleArray):
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


