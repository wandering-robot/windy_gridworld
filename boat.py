from world import Sea

class Boat:
    def __init__(self):

        self.world = Sea()
        self.cell = self.world.starting_cell
        
        self.update_coord()

    def update_coord(self):
        self.x = self.cell.x
        self.y = self.cell.y

    def move(self,delx,dely):
        #keeps boat within bounds of sea
        try:
            intended_cell = self.world.cells[(self.x+delx,self.y+dely)]
        except KeyError:
            if self.x + delx > self.world.x_max or self.x + delx < 0:
                delx = 0
            if self.y + dely > self.world.y_max or self.y + dely < 0:
                dely = 0
            intended_cell = self.world.cells[(self.x+delx,self.y+dely)]
        #keeps wind from pushing too far upwards
        try:
            self.cell = self.world.cells[(self.x+delx,self.y+dely - intended_cell.wind_strength)]
        except KeyError:
            self.cell = intended_cell

        self.update_coord()


if __name__ == "__main__":
    boat = Boat()
    print(f'Boat at ({boat.x},{boat.y})')

    for _ in range(9):
        dir = (1,0)
        boat.move(*dir)
        print(f'Boat at ({boat.x},{boat.y})')

