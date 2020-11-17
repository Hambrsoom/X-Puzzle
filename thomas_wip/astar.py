from pprint import pprint
from bisect import insort 
from successor import generateChildStates
from solution_path import getSolutionPath
from search_path import getSearchPath
from helper_methods import *
import time

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

def astar(puzzleNumber, puzzleArr, numRows, numColumns):
    print("Running A* algo on the following puzzle:")
    print(puzzleArr)

    puzzleDimensions["numRows"] = numRows
    puzzleDimensions["numColumns"] = numColumns

    open = [{
        "currentState": puzzleArr.copy(),
        "parent": None,
        "gn": 0,
        "hn": 0,
        "fn": 0,
        "cost": 0,
        "movedTile": 0
    }]
    closed = []

    goalFound = False

    goalNode = None

    firstSolutionList = generateFirstSolutionList(puzzleArr)
    secondSolutionList = generateSecondSolutionList(numRows, numColumns)

    start_time = time.time()
    time_end = start_time + 60

    while not goalFound and time.time() <= time_end:
        nodeWeAreLookingAt = open.pop(0)
        print(nodeWeAreLookingAt['currentState'])
        closed.insert(0, nodeWeAreLookingAt)

        goalFound = isGoal(nodeWeAreLookingAt['currentState'], puzzleDimensions)
        if goalFound: goalNode = nodeWeAreLookingAt

        #get children, add to open list
        children = generateChildStates(nodeWeAreLookingAt["currentState"], nodeWeAreLookingAt["gn"], puzzleDimensions)
        
        evaluateHeuristicOnChildren(children, puzzleDimensions, firstSolutionList, secondSolutionList)
        evaluateStarFunctionOnChildren(children)
<<<<<<< Updated upstream

        open = admissibilityUpdateOpenList(children, open, closed)
=======
        open.extend(children)
>>>>>>> Stashed changes
        open = sorted(open, key=lambda k: k['fn'])

    execution_time = time.time() - start_time
    
    if time.time() <= time_end:
        getSearchPath(closed, "astar", puzzleNumber, True, "h1")
        getSolutionPath(goalNode, closed, "astar", puzzleNumber, True, "h1", execution_time)
    else: 
        getSearchPath(closed, "astar", puzzleNumber, False, "h1")
        getSolutionPath(goalNode, closed, "astar", puzzleNumber, False, "h1", execution_time)
    

def evaluateStarFunctionOnChildren(children):
    for child in children:
        child["fn"] = child["hn"] + child["gn"]

def admissibilityUpdateOpenList(children, open, closed):
    for child in children:
        isInOpenOrClosed = 0
        for closedElement in closed:
            if child["currentState"] == closedElement["currentState"]:
                isInOpenOrClosed = 1
                if int(child["fn"]) < int(closedElement["fn"]):
                    closed.remove(closedElement)
                    open.append(closedElement)
                    break
        if(isInOpenOrClosed == 0):        
            for element in open:
                if child["currentState"] == element["currentState"]:
                    isInOpenOrClosed = 1
                    if int(child["fn"]) < int(element["fn"]):
                        open[open.index(element)] = child
                        break
        if(isInOpenOrClosed == 0):        
            open.append(child)
        
    return open;       
