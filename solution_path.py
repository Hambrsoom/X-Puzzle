from helper_methods import listToString

# get the solution path and generate the proper txt file for them.
def getSolutionPath(goalNode, closedArr, algoType, puzzleNumber, foundSolution, heuristicFunction, executionTime):
    if heuristicFunction == "":
        fileName = "output/" + str(puzzleNumber) + "_" + algoType + "_solution" +".txt"
    else:
        fileName = "output/" + str(puzzleNumber) + "_" + algoType + "-" + heuristicFunction + "_solution" +".txt"

    file = open(fileName, "w")

    if foundSolution:
        solutionPath = []
        solutionPath.append(goalNode)
        parentState = goalNode["parent"]

        parent = getNodeFromState(parentState, closedArr)

        while parent is not None:
            solutionPath.append(parent)
            parentState = parent["parent"]
            parent = getNodeFromState(parentState, closedArr)

        solutionPath.reverse()

        for node in solutionPath:
            file.write(str(node["movedTile"]) + " " + str(node["cost"]) + " " + listToString(node["currentState"]) + "\n")

        file.write(str(solutionPath[-1]['gn']) + " " + str(executionTime))

    else:
        file.write("no solution")
    file.close()


def getNodeFromState(state, puzzleArr):
    node = None
    try:
        node = next(item for item in puzzleArr if item["currentState"] == state)
        return node
    except StopIteration:
        return None

    return node

    