
class State:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.wind_strength = None

        self.is_terminal = self.find_if_terminal()

        if not(self.is_terminal):       #entering a state gives reward of -1 unless terminal state. Incentiveses getting to terminal as quickly as possible
            self.reward = -1
        else:
            self.reward = 0

    def find_if_terminal(self):
        return (self.x == 7 and self.y == 3) or (self.x == 7 and self.y == 4)

    def __repr__(self):
        return f'State: {self.x},{self.y}'

    def __add__(self,other):
        return(self.x+other.x,self.y+other.y)