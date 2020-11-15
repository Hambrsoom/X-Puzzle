from pprint import pprint
from bisect import insort 
from successor import generateChildStates
from solution_path import getSolutionPath
from helper_methods import *
from search_path import getSearchPath



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
    print("Running Uniform Cost algo on the following puzzle:")

    puzzleDimensions["numRows"] = numRows
    puzzleDimensions["numColumns"] = numColumns

    open = [{
        "currentState": puzzleArr.copy(),
        "parent": None,
        "gn": 0
    }]
    closed = []

    goalFound = False

    goalNode = None

    while(not goalFound):
        nodeWeAreLookingAt = open.pop(0)
        print(nodeWeAreLookingAt['currentState'])
        closed.insert(0, nodeWeAreLookingAt)

        goalFound = isGoal(nodeWeAreLookingAt['currentState'], puzzleDimensions)
        if goalFound: goalNode = nodeWeAreLookingAt

        #get children, add to open list
        children = generateChildStates(nodeWeAreLookingAt["currentState"], nodeWeAreLookingAt["gn"], puzzleDimensions)
        children = removeStatesWeHaveAlreadyVisitedFromChildren(children, closed)
        open.extend(children)
        open = sorted(open, key=lambda k: k['gn'])

    # we will add the getSearchPath here (calling method from another file)

    getSearchPath(closed, "ucs", 1)
    getSolutionPath(goalNode, closed)

