from time import time
from utilities import randomClues
from pysudoku import Grid
from copy import deepcopy
from Naive import solver as ns
from MRV import solver as ms
from MRVPlus import solver as mps

# uncomment either line 11 or line 14 as required
# hardcoded input
# clues = "850002400720000009004000000000107002305000900040000000000080070017000000000036040"

# generating random input
clues = randomClues()

puzzle = Grid(clues)
puzzle.slomo = 0.01
print("Sudoku puzzle:\n"+str(puzzle)+"\n"+"-"*50+"\nSolutions:")

grid = deepcopy(puzzle)
grid.starttime = time()
ns(grid)

grid = deepcopy(puzzle)
grid.starttime = time()
ms(grid)

grid = deepcopy(puzzle)
grid.starttime = time()
mps(grid)