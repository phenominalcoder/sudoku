import random
from time import sleep
from pysudoku import Grid

def inputFormat(matrix):
    clues = ""
    for line in matrix:
        for clue in line:
            clues=clues+str(clue)
    return clues

display = lambda matrix: [print(*line) for line in matrix]

def checkCellConstraints(row,column,number,matrix):
    # Checking for identical number in row or column
    for i in range(0,Grid.grid_size):
        if matrix[row][i] == number or matrix[i][column] == number:
            return False
    # Checking for identical number in sub-grid
    row, column = row-row%Grid.sub_grid_size, column-column%Grid.sub_grid_size
    for i in range(0,Grid.sub_grid_size):
        for j in range(0,Grid.sub_grid_size):
            if matrix[row+i][column+j] == number:
                return False
    # All constraints are met
    return True

def randomClues():
    matrix = [[0 for row in range(Grid.grid_size)] for column in range(Grid.grid_size)]
    count = 0
    count = Grid.grid_size*2-1
    while count > 0:
        row = random.randint(0,Grid.grid_size-1)
        column = random.randint(0,Grid.grid_size-1)
        while matrix[row][column] > 0:
            row = random.randint(0,Grid.grid_size-1)
            column = random.randint(0,Grid.grid_size-1)
        number = random.randint(1,Grid.grid_size)
        if checkCellConstraints(row, column, number, matrix):
            matrix[row][column] = number
            count = count-1
    return inputFormat(matrix)
    
def show(solver, grid):
    print("-"*50)
    print(solver, "Backtracking - ", grid.recursions, "Recursions")
    print("Elapsed time in seconds: ", round(grid.elapsedtime, 6))
    print("-"*50)
    print(grid)

def clean(slomo):
    CURSOR_UP = "\033[1A"
    CLEAR = "\x1b[2K"
    sleep(slomo)
    print((CURSOR_UP + CLEAR) * (Grid.grid_size+5), end="")