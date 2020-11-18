from bisect import insort 
from successor import generateChildStates
from solution_path import getSolutionPath
from helper_methods import *
from search_path import getSearchPath
import time

#file variable
puzzleDimensions = {
    "numRows": 0,
    "numColumns": 0
}

def uniform_cost(puzzleNumber, puzzleArr, numRows, numColumns):

    start_time = time.time()
    time_end = start_time + 600

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
        
        # get the first node from the sorted open list 
        nodeWeAreLookingAt = open.pop(0)
        closed.insert(0, nodeWeAreLookingAt)
        goalFound = isGoal(nodeWeAreLookingAt['currentState'], puzzleDimensions)
        if goalFound: goalNode = nodeWeAreLookingAt

        # get children, add to open list
        children = generateChildStates(nodeWeAreLookingAt["currentState"], nodeWeAreLookingAt["gn"], puzzleDimensions)

        # remove the children already exist in the close list from the children list.
        children = removeStatesWeHaveAlreadyVisitedFromChildren(children, closed)

        # add the children to the open list
        open = addChildrenToOpenList(children, open)

        # sort the open list according to the cost
        open = sorted(open, key = lambda k: k['gn'])

    execution_time = time.time() - start_time
    
    # The type of the solutiona and search files to generate if they pass 60 seconds or not
    if time.time() <= time_end:
        print("< exec time")
        getSearchPath(closed, "ucs", puzzleNumber, True, "")
        getSolutionPath(goalNode, closed, "ucs", puzzleNumber, True, "", execution_time)
    else: 
        print("no solution")
        getSearchPath(closed, "ucs", puzzleNumber, False, "")
        getSolutionPath(goalNode, closed, "ucs", puzzleNumber, False, "", execution_time)


