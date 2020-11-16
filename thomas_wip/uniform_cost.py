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

def uniform_cost(puzzleNumber, puzzleArr, numRows, numColumns):

    start_time = time.time()
    time_end = start_time + 60

    print("Running Uniform Cost algo on the following puzzle:")

    puzzleDimensions["numRows"] = numRows
    puzzleDimensions["numColumns"] = numColumns

    open = [{
        "currentState": puzzleArr.copy(),
        "parent": None,
        "cost": 0,
        "movedTile": 0,
        "gn": 0
    }]
    closed = []

    goalFound = False

    goalNode = None   
    
    while not goalFound and time.time() <= time_end:
        nodeWeAreLookingAt = open.pop(0)
        print(nodeWeAreLookingAt['currentState'])        
        closed.insert(0, nodeWeAreLookingAt)
        goalFound = isGoal(nodeWeAreLookingAt['currentState'], puzzleDimensions)
        if goalFound: goalNode = nodeWeAreLookingAt

        #get children, add to open list
        children = generateChildStates(nodeWeAreLookingAt["currentState"], nodeWeAreLookingAt["gn"], puzzleDimensions)
        children = removeStatesWeHaveAlreadyVisitedFromChildren(children, closed)
        open = addChildrenToOpenList(children, open)
        open = sorted(open, key = lambda k: k['gn'])

    execution_time = time.time() - start_time
    
    if time.time() <= time_end:
        print("< exec time")
        getSearchPath(closed, "ucs", puzzleNumber, True, "")
        getSolutionPath(goalNode, closed, "ucs", puzzleNumber, True, "", execution_time)
    else: 
        print("no sol")
        getSearchPath(closed, "ucs", puzzleNumber, False, "")
        getSolutionPath(goalNode, closed, "ucs", puzzleNumber, False, "", execution_time)


