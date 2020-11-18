from astar import astar
from gbfs import gbfs
from uniform_cost import uniform_cost

def generateSolutionAndSearchFiles(puzzles, nRows, nColumns):
    for index in range(len(puzzles)):
        #uniform_cost(index, puzzles[index], nRows, nColumns)

        gbfs(index, puzzles[index], nRows, nColumns, "h1")
        #gbfs(index, puzzles[index], nRows, nColumns, "h2")

        astar(index, puzzles[index], nRows, nColumns, "h1")
        #astar(index, puzzles[index], nRows, nColumns, "h2")
