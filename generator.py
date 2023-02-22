import random
from sudokuUtils import *
matrix = [[0 for row in range(9)] for column in range(9)]
count = 0
count = random.randint(17,22)
while count > 0:
    row = random.randint(0,8)
    column = random.randint(0,8)
    while matrix[row][column] > 0:
        row = random.randint(0,8)
        column = random.randint(0,8)
    number = random.randint(1,9)
    if checkCellConstraints(row, column, number, matrix):
        matrix[row][column] = number
        count = count-1
display(matrix)