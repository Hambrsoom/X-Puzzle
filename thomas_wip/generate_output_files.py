from astar import astar
from gbfs import gbfs
from uniform_cost import uniform_cost

# The purpose of this method is to run all the algorithms with 
# a list of puzzles. We can also emphasis the type of the puzzle
# to be used by passing the number of rows and columns
def generateSolutionAndSearchFiles(puzzles, nRows, nColumns):
    for index in range(len(puzzles)):
        uniform_cost(index, puzzles[index], nRows, nColumns)

        # gbfs(index, puzzles[index], nRows, nColumns, "h1")
        # gbfs(index, puzzles[index], nRows, nColumns, "h2")

        # astar(index, puzzles[index], nRows, nColumns, "h1")
        # astar(index, puzzles[index], nRows, nColumns, "h2")
