# imports
from argparse import ArgumentParser
from importPuzzles import *
from astar import astar
from gbfs import gbfs
from helper_methods import generateSecondSolutionList
from uniform_cost import uniform_cost
from generate_output_files import generateSolutionAndSearchFiles

# global variables
filePath = "puzzles.txt"

# argument parser with file argument
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-a", "--algo", dest="algo",
                    help="algorithm name", metavar="algo")
args = parser.parse_args()
if args.filename is not None:
    filePath = args.filename

# generate random 50 puzzles of the dimenstion 2*4:
# generateFileOfFiftyPuzzles(2, 4, 50)

# import puzzles
puzzles = importPuzzlesFromFile(filePath)
puzzleNumber = 0

if args.algo == 'gbfs':
    gbfs(puzzleNumber, puzzles[puzzleNumber], 2, 4)
if args.algo == 'astar':
    astar(puzzleNumber, puzzles[0], 2, 4, "h2")
if args.algo == 'ucs':
    uniform_cost(puzzleNumber, puzzles[0], 2, 4)
if args.algo == 'all':
    generateSolutionAndSearchFiles(puzzles, 4, 4)