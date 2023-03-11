from utilities import show, clean

def resolveFoS(grid, potential_positions):
    selected_position = potential_positions[0]
    max_contribution = 0
    max_contributing_number = 0
    for position in potential_positions:
        for number in grid.cells[position].candidates:
            contribution = 0
            for peer in grid.peers[position]:
                if not grid.cells[peer].cellvalue:
                    contribution = contribution+len(grid.cells[position].candidates.intersection(grid.cells[peer].candidates))
            if contribution > max_contribution:
                max_contribution = contribution
                selected_position = position
                max_contributing_number = number
    return selected_position

def solver(grid):
    grid.recursions = grid.recursions+1
    grid.solved = True
    potential_position = None
    potential_positions = None
    min_candidates = grid.grid_size + 1
    for position in grid.cells:
        if not grid.cells[position].cellvalue:
            potential_position = position
            grid.solved = False
            candidates_count = len(grid.cells[position].candidates)
            if candidates_count < min_candidates:
                min_candidates = candidates_count
                potential_positions = [position]
            elif candidates_count == min_candidates:
                potential_positions.append(position)
    position = potential_position
    if potential_positions:
        position = resolveFoS(grid, potential_positions)
    if grid.solved:
        show("MRVPlus", grid)
        return True
    for number in grid.cells[position].candidates:
        if grid.slomo:
            show("MRVPlus", grid)
            clean(grid.slomo)
        grid.cells[position].cellvalue = number
        if solver(grid):
            return True
        grid.cells[position].cellvalue = 0
    return False