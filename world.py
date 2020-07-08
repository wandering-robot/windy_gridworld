from cell import Cell

class Sea:
    def __init__(self):
        self.y_max = 6
        self.x_max = 9
        
        self.cells = {}     #tuple coord as refernce to the cell itself {(coord):cell object}

        self.create_world()

        self.starting_cell = self.cells[(0,4)]
        self.terminal_cell = self.cells[(7,3)]

    def create_world(self):
        for i in range(self.x_max):
            for j in range(self.y_max):
                cell = Cell(i,j):
                self.cells[(i,j)] = cell

