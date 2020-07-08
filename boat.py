from world import World

class Boat:
    def __init__(self):

        self.world = World()
        self.cell = world.starting_cell
        
        self.x = self.cell.x
        self.y = self.cell.y

    def move(self,delx,dely):
        self.cell = self.world[(self.x+delx,self.y+dely)]

