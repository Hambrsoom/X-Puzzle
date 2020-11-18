# Link To GitHub Repository
https://github.com/Hambrsoom/X-Puzzle

# X-Puzzle
The purpose of the project is to implement uniform cost, GBFS and A* algorithms to find the goal in the X-puzzle game. After implementing these algorithms, we compared these algorithms by analyzing the execution time, cost, length of search path and length of solution path. 

## Team Members 👥
| Name          | Student ID    |
| ------------- |:-------------:|
|  Hambrsoom Baboyan | 40054395 |
|  Thomas Gauvin     | 40064853 |
|  Zohal Mir         | 40033246 |

## Requirements
- Have the libraries csv, numpy, random, installed (i.e. pip install csv)
- Make sure that the folder "output" exist in the directory of the project.

## Output Folders
1. output folder: contains the 500 solution and search files produced after running the 50 puzzles (2x4).
2. output3by4 folder: contains the 8 solution and search files produced after running 4 puzzles (3x4). The file puzzles3by4 contains the puzzles that were used. (ran on gbfs-h1)
3. output4by4 folder: contains the 6 solution and search files produced after running 3 puzzles (4x4). The file puzzles4by4 contains the puzzles that were used. (ran on gbfs-h1)


## Compile and Running
1. Clone the repository.
2. Open the command line in the directory.
3. To run the first puzzle in the puzzles.txt file, you can run it on one of the algorithms: *A**, *GBFS* or *UCS* by running the command line: 
  *python run.py -a astar*, *python run.py -a gbfs*, *python run.py -a ucs* respectively.
4. You can run all the puzzles by the command line: *python run.py -a all*
5. You can find the solution and search out files in the *output* folder.  
6. You can run the analysis on these output files by running the command python: *python analysis.py*
7. You can see the result output file in the directory of the project under the file name: *analysisResults.txt*

