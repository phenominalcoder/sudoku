getMatrix = lambda file_path: [list(map(int, line.replace("'","").split(" ")))\
            for line in open(file_path.replace("'",""),'r').read().split("\n") if len(line)>0]

display = lambda matrix: [print(*line) for line in matrix]

def checkCellConstraints(row,column,number,matrix):
    # Checking for identical number in row or column
    for i in range(0,9):
        if matrix[row][i] == number or matrix[i][column] == number:
            return False
    # Checking for identical number in sub-grid
    row, column = row-row%3, column-column%3
    for i in range(0,3):
        for j in range(0,3):
            if matrix[row+i][column+j] == number:
                return False
    # All constraints are met
    return True

class Calls:
	count = 0
