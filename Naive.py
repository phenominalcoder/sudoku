from sudokuUtils import *

calls = Calls()

def solver(matrix):
	calls.count = calls.count+1
	solved = True
    # Looking for a cell containing 0
	for i in range(0,9):
		for j in range(0,9):
			if matrix[i][j] == 0:
				solved = False
				row = i
				column = j
				break
	if solved:
		display(matrix)
		print("Naive Backtracking - ", calls.count, "Recursions")
		return True
    # Trying to fill current cell to move forward / backtrack as required
	for number in range(1, 10):
		if checkCellConstraints(row, column, number, matrix):
			matrix[row][column] = number
			if solver(matrix):
				return True
			matrix[row][column] = 0
	return False