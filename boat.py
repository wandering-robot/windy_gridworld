from world import World

class Boat:
    def __init__(self):

        self.world = World()
        self.state = self.world.starting_state
        
        self.coord = self.update_coord()

    def update_coord(self):
        self.x = self.state.x
        self.y = self.state.y
        return self.x,self.y

    def move(self,delx,dely):
        #keeps boat within bounds of sea
        try:
            intended_state = self.world.states[(self.x+delx,self.y+dely)]
        except KeyError:
            if self.x + delx > self.world.x_max or self.x + delx < 0:
                delx = 0
            if self.y + dely > self.world.y_max or self.y + dely < 0:
                dely = 0
            intended_state = self.world.states[(self.x+delx,self.y+dely)]
        #keeps wind from pushing too far upwards
        try:
            self.state = self.world.states[(self.x+delx,self.y+dely - intended_state.wind_strength)]
        except KeyError:
            self.state = intended_state

        self.coord = self.update_coord()


if __name__ == "__main__":
    boat = Boat()
    print(f'Boat at ({boat.x},{boat.y})')

    for _ in range(9):
        dir = (1,0)
        boat.move(*dir)
        print(f'Boat at ({boat.x},{boat.y})')

