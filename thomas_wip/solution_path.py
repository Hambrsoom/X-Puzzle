from pprint import pprint
from helper_methods import listToString

def getSolutionPath(goalNode, closedArr, algoType, puzzleNumber, foundSolution, heuristicFunction, executionTime):
    print("========================")
    print("Solution Path")
    print("========================")

    if heuristicFunction == "":
        fileName = "output/" + str(puzzleNumber) + "_" + algoType + "_solution" +".txt"
    else:
        fileName = "output/" + str(puzzleNumber) + "_" + algoType + "-" + heuristicFunction + "_solution" +".txt"

    file = open(fileName, "w")

    print(foundSolution)

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
        pprint(solutionPath)
        print('cost of solution:')
        pprint(solutionPath[-1]['gn']) 
        print('count of edges of solution:')
        pprint(len(solutionPath))
        print('len of search path')
        pprint(len(closedArr))

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

    