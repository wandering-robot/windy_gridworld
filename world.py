from state import State

class World:
    def __init__(self):
        self.y_max = 6
        self.x_max = 9
        
        self.wind_strength_list = [0,0,0,1,1,1,2,2,1,0]

        self.states = {}     #tuple coord as refernce to the state itself {(coord):state object}

        self.create_world()

        self.starting_state = self.states[(0,3)]
        self.terminal_state = self.states[(7,3)]

    def create_world(self):
        for i in range(self.x_max+1):
            for j in range(self.y_max+1):
                state = State(i,j)
                state.wind_strength = self.wind_strength_list[i]
                self.states[(i,j)] = state

if __name__ == "__main__":
    world = World()
    print(world.states)
