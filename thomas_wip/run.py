# imports
from argparse import ArgumentParser
from importPuzzles import importPuzzlesFromFile
from heuristics import h0
from astar import astar
from gbfs import gbfs
from uniform_cost import uniform_cost

# global variables
filePath = "samplePuzzles.txt"

# argument parser with file argument
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-a", "--algo", dest="algo",
                    help="algorithm name", metavar="algo")
args = parser.parse_args()
if args.filename is not None:
    filePath = args.filename

# import puzzles
puzzles = importPuzzlesFromFile(filePath)

if args.algo == 'gbfs':
    gbfs(puzzles[4], 2, 4)
if args.algo == 'astar':
    astar(puzzles[4], 2, 4)
if args.algo == 'uc':
    uniform_cost(puzzles[4], 2, 4)
