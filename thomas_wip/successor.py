
# generating the next moves (by anticipating the possible moves) and then return a list of children
# which can be considered as next step to reach to the goal state.
def generateChildStates(puzzleArr, gn, puzzleDimensions):
    children = []

    zeroTileIndex = puzzleArr.index('0')

    #regular moves
    if isLeftEdge(zeroTileIndex, puzzleArr, puzzleDimensions) == False:
        move, movedTile = generateMoveLeft(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 1,
            "gn": gn+1
        })
    if isRightEdge(zeroTileIndex, puzzleArr, puzzleDimensions) == False:
        move, movedTile = generateMoveRight(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 1,
            "gn": gn+1
        })
    if isBottomEdge(zeroTileIndex, puzzleArr, puzzleDimensions) == False:
        move, movedTile = generateMoveBottom(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 1,
            "gn": gn+1
        })
    if isTopEdge(zeroTileIndex, puzzleArr, puzzleDimensions) == False:
        move, movedTile = generateMoveTop(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 1,
            "gn": gn+1
        })

    #wrapping move
    if isTopEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isLeftEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = generateWrapLeftEdge(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 2,
            "gn": gn+2
        })
    if isBottomEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isLeftEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = generateWrapLeftEdge(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 2,
            "gn": gn+2
        })
    if isTopEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isRightEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = generateWrapRightEdge(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 2,
            "gn": gn+2
        })
    if isBottomEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isRightEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = generateWrapRightEdge(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 2,
            "gn": gn+2
        })

    #diagonal move
    if isTopEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isLeftEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = swapTopLeftCorner(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
        move, movedTile = generateDiagonalTopLeft(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
    if isTopEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isRightEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = swapTopRightCorner(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
        move, movedTile = generateDiagonalTopRight(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
    if isBottomEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isLeftEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = swapBottomLeftCorner(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
        move, movedTile = generateDiagonalBottomLeft(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
    if isBottomEdge(zeroTileIndex, puzzleArr, puzzleDimensions) and isRightEdge(zeroTileIndex, puzzleArr, puzzleDimensions):
        move, movedTile = swapRightBottomCorner(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
        move, movedTile = generateDiagonalBottomRight(zeroTileIndex, puzzleArr.copy(), puzzleDimensions)
        children.append({
            "currentState": move,
            "parent": puzzleArr,
            "movedTile": movedTile,
            "cost": 3,
            "gn": gn + 3
        })
    
    return children


def isLeftEdge(puzzleTileIndex, puzzleArr, puzzleDimensions):
    return puzzleTileIndex % puzzleDimensions["numColumns"] == 0

def isRightEdge(puzzleTileIndex, puzzleArr, puzzleDimensions):
    return (puzzleTileIndex + 1) % puzzleDimensions["numColumns"] == 0

def isTopEdge(puzzleTileIndex, puzzleArr, puzzleDimensions):
    return puzzleTileIndex < puzzleDimensions["numColumns"]

def isBottomEdge(puzzleTileIndex, puzzleArr, puzzleDimensions):
    return puzzleTileIndex > (puzzleDimensions["numColumns"] * puzzleDimensions["numRows"]) - puzzleDimensions["numColumns"] - 1


def generateDiagonalBottomRight(index, puzzleArr, puzzleDimensions): #when zero in top left
    n = (puzzleDimensions["numRows"]-1) * puzzleDimensions["numColumns"] - 2
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def generateDiagonalBottomLeft(index, puzzleArr, puzzleDimensions): #when zero in top left
    n = (puzzleDimensions["numRows"]-2) * puzzleDimensions["numColumns"] + 1
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def generateDiagonalTopRight(index, puzzleArr, puzzleDimensions): #when zero in top left
    n = 2*puzzleDimensions["numColumns"] - 2
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def generateDiagonalTopLeft(index, puzzleArr, puzzleDimensions): #when zero in top left
    n = puzzleDimensions["numColumns"] + 1
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def swapBottomLeftCorner(index, puzzleArr, puzzleDimensions): #when zero in bottom left corner, swap with top right corner
    n = puzzleDimensions["numColumns"] - 1 
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def swapTopRightCorner(index, puzzleArr, puzzleDimensions): #when zero in top right corner, swap with bottom left corner
    n = (puzzleDimensions["numRows"]-1) * puzzleDimensions["numColumns"] + 1 
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def swapTopLeftCorner(index, puzzleArr, puzzleDimensions): #when zero in top left corner, swap with bottom right corner
    n = puzzleDimensions["numRows"] * puzzleDimensions["numColumns"] - 1
    puzzleArr[n], puzzleArr[index] = puzzleArr[index], puzzleArr[n]
    return puzzleArr, puzzleArr[index]

def swapRightBottomCorner(index, puzzleArr, puzzleDimensions): #when zero in bottom right corner, swap with top left corner
    puzzleArr[0], puzzleArr[index] = puzzleArr[index], puzzleArr[0]
    return puzzleArr, puzzleArr[index]

def generateWrapRightEdge(index, puzzleArr, puzzleDimensions): #when zero on right edge
    n = puzzleDimensions["numColumns"]
    newIndex = index - n + 1
    puzzleArr[newIndex], puzzleArr[index] = puzzleArr[index], puzzleArr[newIndex]
    return puzzleArr, puzzleArr[index]

def generateWrapLeftEdge(index, puzzleArr, puzzleDimensions): #when zero on left edge
    n = puzzleDimensions["numColumns"]
    newIndex = index + n - 1
    puzzleArr[newIndex], puzzleArr[index] = puzzleArr[index], puzzleArr[newIndex]
    return puzzleArr, puzzleArr[index]

def generateMoveTop(index, puzzleArr, puzzleDimensions):
    n = puzzleDimensions["numColumns"]
    puzzleArr[index-n], puzzleArr[index] = puzzleArr[index], puzzleArr[index-n]
    return puzzleArr, puzzleArr[index]

def generateMoveBottom(index, puzzleArr, puzzleDimensions):
    n = puzzleDimensions["numColumns"]
    puzzleArr[index+n], puzzleArr[index] = puzzleArr[index], puzzleArr[index+n]
    return puzzleArr, puzzleArr[index]

def generateMoveRight(index, puzzleArr, puzzleDimensions):
    puzzleArr[index+1], puzzleArr[index] = puzzleArr[index], puzzleArr[index+1]
    return puzzleArr, puzzleArr[index]

def generateMoveLeft(index, puzzleArr, puzzleDimensions):
    puzzleArr[index-1], puzzleArr[index] = puzzleArr[index], puzzleArr[index-1]
    return puzzleArr, puzzleArr[index]
