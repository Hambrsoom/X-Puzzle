from pprint import pprint
from bisect import insort 
from heuristics import h0 as desiredHeuristic

# sampleStateSpace = {
#     "currentState": [1,2,3,4,5,6,7,0],
#     "parent": [1,2,3,5,4,6,7,0],
#     "gn": 2,
#     "hn": 4
# }

#file variable
puzzleDimensions = {
    "numRows": 0,
    "numColumns": 0
}

def uniform_cost(puzzleArr, numRows, numColumns):
    print("Running A* algo on the following puzzle:")
    print(puzzleArr)

    puzzleDimensions["numRows"] = numRows
    puzzleDimensions["numColumns"] = numColumns

    open = [{
        "currentState": puzzleArr.copy(),
        "parent": None,
        "gn": 0,
        "hn": 0
    }]
    closed = []

    goalFound = False

    goalNode = None

    while(not goalFound):
        nodeWeAreLookingAt = open.pop(0)
        print(nodeWeAreLookingAt['currentState'])
        closed.insert(0, nodeWeAreLookingAt)

        goalFound = isGoal(nodeWeAreLookingAt['currentState'])
        if goalFound: goalNode = nodeWeAreLookingAt

        #get children, add to open list
        children = generateChildStates(nodeWeAreLookingAt["currentState"], nodeWeAreLookingAt["gn"])
        children = removeStatesWeHaveAlreadyVisitedFromChildren(children, closed)
        evaluateHeuristicOnChildren(children)
        open.extend(children)
        open = sorted(open, key=lambda k: k['gn'])
    
    print("========================")
    print("Search Path")
    print("========================")
    pprint(closed)

    print("========================")
    print("Solution Path")
    print("========================")
    solutionPath = getSolutionPath(goalNode, closed)
    solutionPath.reverse()
    pprint(solutionPath)
    print('cost of solution:')
    pprint(solutionPath[-1]['gn']) 
    print('count of edges of solution:')
    pprint(len(solutionPath))
    print('len of search path')
    pprint(len(closed))

def getSolutionPath(goalNode, closedArr):
    solutionPath = []
    solutionPath.append(goalNode)
    parentState = goalNode["parent"]

    parent = getNodeFromState(parentState, closedArr)

    while parent is not None:
        solutionPath.append(parent)
        parentState = parent["parent"]
        parent = getNodeFromState(parentState, closedArr)

    return solutionPath

def getNodeFromState(state, puzzleArr):
    node = None
    try:
        node = next(item for item in puzzleArr if item["currentState"] == state)
        return node
    except StopIteration:
        return None

    return node

def removeStatesWeHaveAlreadyVisitedFromChildren(children, closed):
    cleanChildren = children.copy()
    for child in cleanChildren:
        for closedState in closed:
            if isSameState(child, closedState):
                children.remove(child)
                break

    return children

def evaluateHeuristicOnChildren(children):
    for child in children:
        child["hn"] = desiredHeuristic(child['currentState'])

def isGoal(puzzleArr):
    return increasingHorizontallyWithBottomRightCorner0(puzzleArr) or increasingVerticallyWithBottomRightCorner0(puzzleArr)

def increasingHorizontallyWithBottomRightCorner0(puzzleArr):
    arrCopy = puzzleArr.copy()
    lastIsZero = arrCopy.pop() == '0'
    return lastIsZero and all(int(puzzleArr[i]) <= int(puzzleArr[i+1]) for i in range(len(puzzleArr)-2)) #-2 since pop

def increasingVerticallyWithBottomRightCorner0(puzzleArr):
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

    return lastIsZero

def generateChildStates(puzzleArr, gn):
    children = []

    zeroTileIndex = puzzleArr.index('0')

    #regular moves
    if isLeftEdge(zeroTileIndex, puzzleArr) == False:
        children.append({
            "currentState": generateMoveLeft(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+1
        })
    if isRightEdge(zeroTileIndex, puzzleArr) == False:
        children.append({
            "currentState": generateMoveRight(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+1
        })
    if isBottomEdge(zeroTileIndex, puzzleArr) == False:
        children.append({
            "currentState": generateMoveBottom(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+1
        })
    if isTopEdge(zeroTileIndex, puzzleArr) == False:
        children.append({
            "currentState": generateMoveTop(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+1
        })

    #wrapping move
    if isTopEdge(zeroTileIndex, puzzleArr) and isLeftEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": generateWrapLeftEdge(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+2
        })
    if isBottomEdge(zeroTileIndex, puzzleArr) and isLeftEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": generateWrapLeftEdge(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+2
        })
    if isTopEdge(zeroTileIndex, puzzleArr) and isRightEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": generateWrapRightEdge(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+2
        })
    if isBottomEdge(zeroTileIndex, puzzleArr) and isRightEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": generateWrapRightEdge(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn+2
        })

    #diagonal move
    if isTopEdge(zeroTileIndex, puzzleArr) and isLeftEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": swapTopLeftCorner(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
        children.append({
            "currentState": generateDiagonalTopLeft(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
    if isTopEdge(zeroTileIndex, puzzleArr) and isRightEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": swapTopRightCorner(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
        children.append({
            "currentState": generateDiagonalTopRight(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
    if isBottomEdge(zeroTileIndex, puzzleArr) and isLeftEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": swapBottomLeftCorner(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
        children.append({
            "currentState": generateDiagonalBottomLeft(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
    if isBottomEdge(zeroTileIndex, puzzleArr) and isRightEdge(zeroTileIndex, puzzleArr):
        children.append({
            "currentState": swapRightBottomCorner(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
        children.append({
            "currentState": generateDiagonalBottomRight(zeroTileIndex, puzzleArr.copy()),
            "parent": puzzleArr,
            "gn": gn + 3
        })
    
    return children

def generateDiagonalBottomRight(index, puzzleArr): #when zero in top left
    n = (puzzleDimensions["numRows"]-1) * puzzleDimensions["numColumns"] - 2
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def generateDiagonalBottomLeft(index, puzzleArr): #when zero in top left
    n = (puzzleDimensions["numRows"]-2) * puzzleDimensions["numColumns"] + 1
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def generateDiagonalTopRight(index, puzzleArr): #when zero in top left
    n = 2*puzzleDimensions["numColumns"] - 2
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def generateDiagonalTopLeft(index, puzzleArr): #when zero in top left
    n = puzzleDimensions["numColumns"] + 1
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def swapBottomLeftCorner(index, puzzleArr): #when zero in bottom left corner, swap with top right corner
    n = puzzleDimensions["numColumns"] - 1 
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def swapTopRightCorner(index, puzzleArr): #when zero in top right corner, swap with bottom left corner
    n = (puzzleDimensions["numRows"]-1) * puzzleDimensions["numColumns"] + 1 
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def swapTopLeftCorner(index, puzzleArr): #when zero in top left corner, swap with bottom right corner
    n = puzzleDimensions["numRows"] * puzzleDimensions["numColumns"] - 1
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr

def swapRightBottomCorner(index, puzzleArr): #when zero in bottom right corner, swap with top left corner
    puzzleArr[0], puzzleArr[index] = puzzleArr[index], puzzleArr[0]
    return puzzleArr

def generateWrapRightEdge(index, puzzleArr): #when zero on right edge
    n = puzzleDimensions["numColumns"]
    newIndex = index - n + 1
    puzzleArr[newIndex], puzzleArr[index] = puzzleArr[index], puzzleArr[newIndex]
    return puzzleArr

def generateWrapLeftEdge(index, puzzleArr): #when zero on left edge
    n = puzzleDimensions["numColumns"]
    newIndex = index + n - 1
    puzzleArr[newIndex], puzzleArr[index] = puzzleArr[index], puzzleArr[newIndex]
    return puzzleArr

def generateMoveTop(index, puzzleArr):
    n = puzzleDimensions["numColumns"]
    puzzleArr[index-n], puzzleArr[index] = puzzleArr[index], puzzleArr[index-n]
    return puzzleArr

def generateMoveBottom(index, puzzleArr):
    n = puzzleDimensions["numColumns"]
    puzzleArr[index+n], puzzleArr[index] = puzzleArr[index], puzzleArr[index+n]
    return puzzleArr

def generateMoveRight(index, puzzleArr):
    puzzleArr[index+1], puzzleArr[index] = puzzleArr[index], puzzleArr[index+1]
    return puzzleArr

def generateMoveLeft(index, puzzleArr):
    puzzleArr[index-1], puzzleArr[index] = puzzleArr[index], puzzleArr[index-1]
    return puzzleArr

def isLeftEdge(puzzleTileIndex, puzzleArr):
    return puzzleTileIndex % puzzleDimensions["numColumns"] == 0

def isRightEdge(puzzleTileIndex, puzzleArr):
    return (puzzleTileIndex + 1) % puzzleDimensions["numColumns"] == 0

def isTopEdge(puzzleTileIndex, puzzleArr):
    return puzzleTileIndex < puzzleDimensions["numColumns"]

def isBottomEdge(puzzleTileIndex, puzzleArr):
    return puzzleTileIndex > (puzzleDimensions["numColumns"] * puzzleDimensions["numRows"]) - puzzleDimensions["numColumns"] - 1

def isSameState(dict1, dict2):
    return dict1["currentState"] == dict2["currentState"]