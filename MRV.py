from sudokuUtils import *

calls = Calls()

def solver(matrix):
	calls.count = calls.count+1
	solved = True
	# Looking for a cell containing 0
	cells_candidates_list = []
	for i in range(0,9):
		for j in range(0,9):
			if matrix[i][j] == 0:
				solved = False
				cell_candidates =[]
				cell_candidates.append([i,j])
				candidates = []
				for number in range(1, 10):
					if checkCellConstraints(i, j, number, matrix):
						candidates.append(number)
				cell_candidates.append(len(candidates))
				cell_candidates.append(candidates)
				cells_candidates_list.append(cell_candidates)
	if solved:
		display(matrix)
		print("MRV Backtracking -", calls.count, "Recursions")
		return True
	potential_cell = cells_candidates_list[0]
	lessMRV = cells_candidates_list[0][1]
	cell_candidates = cells_candidates_list[0][2]
	for i in range(1,len(cells_candidates_list)):
		if cells_candidates_list[i][1] < lessMRV:
			potential_cell = cells_candidates_list[i]
			lessMRV = cells_candidates_list[i][1]
	row = potential_cell[0][0]
	column = potential_cell[0][1]
	cell_candidates = potential_cell[2]
    # Trying to fill current cell to move forward | backtrack as required
	for number in cell_candidates:
		matrix[row][column] = number
		if solver(matrix):
			return True
		matrix[row][column] = 0
	return False