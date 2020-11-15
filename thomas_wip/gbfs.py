from pprint import pprint
from bisect import insort 
from successor import generateChildStates
from solution_path import getSolutionPath
from helper_methods import *
from search_path import getSearchPath
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

def gbfs(puzzleNumber, puzzleArr, numRows, numColumns):
    print("Running A* algo on the following puzzle:")
    print(puzzleArr)

    puzzleDimensions["numRows"] = numRows
    puzzleDimensions["numColumns"] = numColumns

    open = [{
        "currentState": puzzleArr.copy(),
        "parent": None,
        "gn": 0,
        "hn": 0,
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
        children = removeStatesWeHaveAlreadyVisitedFromChildren(children, closed)
        evaluateHeuristicOnChildren(children, puzzleDimensions, firstSolutionList, secondSolutionList)
        open.extend(children)
        open = sorted(open, key=lambda k: k['hn'])

    execution_time = time.time() - start_time
    
    if execution_time <= time_end:
        getSearchPath(closed, "gbfs", puzzleNumber, True, "h1")
        getSolutionPath(goalNode, closed, "gbfs", puzzleNumber, True, "h1", execution_time)
    else: 
        getSearchPath(closed, "gbfs", puzzleNumber, False, "h1")
        getSolutionPath(goalNode, closed, "gbfs", puzzleNumber, False, "h1", execution_time)

    # solutionPath = getSolutionPath(goalNode, closed)

