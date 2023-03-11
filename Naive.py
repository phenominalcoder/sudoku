from utilities import show, clean

def solver(grid):
    grid.recursions = grid.recursions+1
    grid.solved = True
    for position in grid.cells:
        if not grid.cells[position].cellvalue:
            grid.solved = False
            break
    if grid.solved:
        show("Naive", grid)
        return True
    for number in grid.cells[position].candidates:
        if grid.slomo:
            show("Naive", grid)
            clean(grid.slomo)
        grid.cells[position].cellvalue = number
        if solver(grid):
            return True
        grid.cells[position].cellvalue = 0
    return False