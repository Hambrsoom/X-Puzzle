from pprint import pprint

def getSolutionPath(goalNode, closedArr):
    print("========================")
    print("Solution Path")
    print("========================")

    solutionPath = []
    solutionPath.append(goalNode)
    parentState = goalNode["parent"]

    parent = getNodeFromState(parentState, closedArr)

    while parent is not None:
        solutionPath.append(parent)
        parentState = parent["parent"]
        parent = getNodeFromState(parentState, closedArr)

    solutionPath.reverse()
    pprint(solutionPath)
    print('cost of solution:')
    pprint(solutionPath[-1]['gn']) 
    print('count of edges of solution:')
    pprint(len(solutionPath))
    print('len of search path')
    pprint(len(closedArr))


def getNodeFromState(state, puzzleArr):
    node = None
    try:
        node = next(item for item in puzzleArr if item["currentState"] == state)
        return node
    except StopIteration:
        return None

    return node