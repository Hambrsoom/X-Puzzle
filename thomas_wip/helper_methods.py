from heuristics import h1 as desiredHeuristic
# h0
# h1 -> Hamming
# h2 -> Manhattan
# h3 -> sumOfPermutationInversions


def removeStatesWeHaveAlreadyVisitedFromChildren(children, closed):
    cleanChildren = children.copy()
    for child in cleanChildren:
        for closedState in closed:
            if isSameState(child, closedState):
                children.remove(child)
                break

    return children

def evaluateHeuristicOnChildren(children, puzzleDimensions):
    for child in children:
        child["hn"] = desiredHeuristic(child['currentState'], puzzleDimensions["numColumns"], puzzleDimensions["numRows"])


def isGoal(puzzleArr, puzzleDimensions):
    return increasingHorizontallyWithBottomRightCorner0(puzzleArr) or increasingVerticallyWithBottomRightCorner0(puzzleArr, puzzleDimensions)

def increasingHorizontallyWithBottomRightCorner0(puzzleArr):
    arrCopy = puzzleArr.copy()
    lastIsZero = arrCopy.pop() == '0'
    return lastIsZero and all(int(arrCopy[i]) <= int(arrCopy[i+1]) for i in range(len(arrCopy)-1)) #-1 since pop

def increasingVerticallyWithBottomRightCorner0(puzzleArr, puzzleDimensions):
    arrCopy = puzzleArr.copy()
    lastIsZero = arrCopy.pop() == '0'

    if lastIsZero == False:
        return False
    n = puzzleDimensions["numColumns"]
    m = puzzleDimensions["numRows"]
    for i in range(n): #iterate through columns
        
        tmp = int(arrCopy[i])
        for j in range(m): #iterate through rows
            if i + j*n >= m*n-1: #-1 to account for popped 0
                break #we've reached the last row
            tmp2 = int(arrCopy[i + j*n])
            if tmp == tmp2:
                continue
            else:
                if tmp2 != tmp + 1:
                    return False
                else:
                    tmp = tmp2
        if i != n and (tmp + m) != int(arrCopy[i+1]):
            return False

    return lastIsZero

def isSameState(dict1, dict2):
    return dict1["currentState"] == dict2["currentState"]