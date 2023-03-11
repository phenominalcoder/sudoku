from time import time

class Grid:
    grid_size = 9
    sub_grid_size = 3
    positions = []
    peers = {}

    @staticmethod
    def fillPositions():
        for row in range(Grid.grid_size):
            for column in range(Grid.grid_size):
                Grid.positions.append((row, column))

    @staticmethod
    def fillPeers():
        Grid.fillPositions()
        for current_position in Grid.positions:
            Grid.peers[current_position] = []
            current_row, current_column = current_position
            for position in Grid.positions:
                if current_position == position:
                    continue
                row, column = position
                sub_grid_row = current_row - current_row % Grid.sub_grid_size
                sub_grid_column = current_column - current_column % Grid.sub_grid_size
                if (row == current_row) or (column == current_column) or \
                    (row in range(sub_grid_row, sub_grid_row + Grid.sub_grid_size)) and \
                    column in range(sub_grid_column, sub_grid_column+ Grid.sub_grid_size):
                    Grid.peers[current_position].append((row, column))

    def refresh(self):
        for current_position in Grid.positions:
            if not self.cells[current_position].cellvalue:
                self.cells[current_position].candidates = set(range(1,Grid.grid_size+1))
                for position in Grid.peers[current_position]:
                    if self.cells[position].cellvalue in self.cells[current_position].candidates:
                        self.cells[current_position].candidates.remove(self.cells[position].cellvalue)

    def __init__(self, clues):
        self.capacity = Grid.grid_size * Grid.grid_size
        self.clues = clues
        self.cells = {}
        self.recursions = 0
        self.starttime = time()
        self._elapsedtime = time() - self.starttime
        self.slomo = 0
        self.solved = False
        clues_iter = iter(clues) 
        for position in Grid.positions:
            number = int(next(clues_iter))
            self.cells[position] = Cell(self, position, number)
        self.refresh()
    
    @property
    def elapsedtime(self):
        return time() - self.starttime

    def __str__(self):
        output = ""
        for row in range(Grid.grid_size):
            for column in range(Grid.grid_size):
                if column<Grid.grid_size-1:
                    output = output+str(self.cells[(row,column)].cellvalue)+" "
                else:
                    output = output+str(self.cells[(row,column)].cellvalue)+"\n"
        return output

class Cell:
    def __init__(self, grid, position, number):
        self.candidates = set()
        self.grid = grid
        self._cellvalue = number
    
    @property
    def cellvalue(self):
        return self._cellvalue
    
    @cellvalue.setter
    def cellvalue(self, number):
        self._cellvalue = number
        if number:
            self.candidates = set()
            self.grid.refresh()

Grid.fillPeers()