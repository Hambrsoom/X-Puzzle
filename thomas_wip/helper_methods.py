from heuristics import hammingDistance, manhattan

# Remove from the children list the nodes which already exist in the closed list
# Then return the new children list
def removeStatesWeHaveAlreadyVisitedFromChildren(children, closed):
    cleanChildren = children.copy()
    for child in cleanChildren:
        for closedState in closed:
            if isSameState(child, closedState):
                children.remove(child)
                break

    return children

# Add the childrent to the open list, make sure that if the child already exist in
# the open list, we check if the new child has a lower or higher cost. if the child
# has a lower case, then we swap it with the node that exists in the open list.
def addChildrenToOpenList(children, open):
    if len(open) > 0 :
        for child in children:
            updatedInOpen = 0
            for element in open:
                if child["currentState"] == element["currentState"]:
                    updatedInOpen = 1
                    if int(child["gn"]) < int(element["gn"]):
                        open[open.index(element)] = child
                        break

            if(updatedInOpen == 0):
                open.append(child)
    else:
        open.extend(children)
        
    return open;

def evaluateHeuristicOnChildren(children, puzzleDimensions, firstSolutionList, secondSolutionList, heuristicType):
    for child in children:
        if heuristicType == "h1":
            child["hn"] = hammingDistance(child['currentState'], puzzleDimensions["numColumns"], puzzleDimensions["numRows"], firstSolutionList, secondSolutionList)
        elif heuristicType == "h2":
            child["hn"] = manhattan(child['currentState'], puzzleDimensions["numColumns"], puzzleDimensions["numRows"], firstSolutionList, secondSolutionList)

# Check if the puzzles has achieved one of the proper goals
def isGoal(puzzleArr, puzzleDimensions):
    return increasingHorizontallyWithBottomRightCorner0(puzzleArr) or increasingVerticallyWithBottomRightCorner0(puzzleArr, puzzleDimensions)

# The method will check if the puzzle has reached this state:
# [[1 2 3 4]
#  [5 6 7 0]]
def increasingHorizontallyWithBottomRightCorner0(puzzleArr):
    arrCopy = puzzleArr.copy()
    lastIsZero = arrCopy.pop() == '0'
    return lastIsZero and all(int(arrCopy[i]) <= int(arrCopy[i+1]) for i in range(len(arrCopy)-1)) #-1 since pop

# The method will check if the puzzle has reached this state:
# [[1 2 3 4]
#  [5 6 7 0]]
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


def generateFirstSolutionList(puzzleArray):
    properList = []
    for number in range(len(puzzleArray)):
        properList.append(number+1)
    
    properList[-1] = 0
    return properList

def generateSecondSolutionList(nRows, nColumns):
    properList = []
    tempList = []
    firstValue = 1

    for i in range(nRows):
        for j in range(nColumns):
            if j == 0:
                tempList.append(firstValue)
            elif i == nRows-1 and j == nColumns-1:
                tempList.append(0)
            else:
                tempList.append( tempList[j-1] + nRows )
        properList = properList + tempList
        tempList = []
        firstValue = firstValue + 1 
    return properList


def listToString(state):  
    str1 = ""  
    
    for element in state:  
        str1 += str(element) + " "
    
    return str1 
