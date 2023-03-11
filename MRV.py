from utilities import show, clean

def solver(grid):
    grid.recursions = grid.recursions+1
    grid.solved = True
    potential_position = None
    min_candidates = grid.grid_size + 1
    for position in grid.cells:
        if not grid.cells[position].cellvalue:
            grid.solved = False
            candidates_count = len(grid.cells[position].candidates)
            if candidates_count < min_candidates:
                min_candidates = candidates_count
                potential_position = position
    position = potential_position
    if grid.solved:
        show("MRV", grid)
        return True
    for number in grid.cells[position].candidates:
        if grid.slomo:
            show("MRV", grid)
            clean(grid.slomo)
        grid.cells[position].cellvalue = number
        if solver(grid):
            return True
        grid.cells[position].cellvalue = 0
    return False