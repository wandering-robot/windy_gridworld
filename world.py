from cell import Cell

class Sea:
    def __init__(self):
        self.y_max = 6
        self.x_max = 9
        
        self.wind_strength_list = [0,0,0,1,1,1,2,2,1,0]

        self.cells = {}     #tuple coord as refernce to the cell itself {(coord):cell object}

        self.create_world()

        self.starting_cell = self.cells[(0,3)]
        self.terminal_cell = self.cells[(7,3)]

    def create_world(self):
        for i in range(self.x_max+1):
            for j in range(self.y_max+1):
                cell = Cell(i,j)
                cell.wind_strength = self.wind_strength_list[i]
                self.cells[(i,j)] = cell

if __name__ == "__main__":
    sea = Sea()
    print(sea.cells)
