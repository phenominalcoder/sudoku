from sudokuUtils import *

calls = Calls()

# Identifies best potential cell based on contribution 
def FogResolver(potential_cells_list, cells_candidates_list):
    selected_cell = potential_cells_list[0]
    max_contribution = 0
    for potential_cell in potential_cells_list:
        for number in potential_cell[2]:
            contribution = 0
            for cell in cells_candidates_list:
                contribution = contribution+len(set(potential_cell[2]).intersection(set(cell[2])))
            if contribution > max_contribution:
                max_contribution = contribution
                selected_cell = potential_cell
    return selected_cell

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
        print("MRVPlus Backtracking -", calls.count, "Recursions")
        return True
    lessMRV = cells_candidates_list[0][1]
    for i in range(1,len(cells_candidates_list)):
        if cells_candidates_list[i][1] < lessMRV:
            lessMRV = cells_candidates_list[i][1]
    potential_cells_list = []
    for cell in cells_candidates_list:
        if cell[1] == lessMRV:
            potential_cells_list.append(cell)
    potential_cell = potential_cells_list[0]
    if len(potential_cells_list) > 1:
        # Fog of search situation
        potential_cell = FogResolver(potential_cells_list, cells_candidates_list)
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