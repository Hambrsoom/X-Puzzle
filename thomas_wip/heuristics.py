def h0(puzzleArray):
    if puzzleArray[-1] == '0':
        return 0
    else:
        return 1

#manhattan
def h1(puzzleArray, xDim, yDim):
    index = puzzleArray.indexOf('0')
    distance = 