
class Q:
    def __init__(self,state,action):
        self.value = 0
        self.state = state
        self.action = action

    def __repr__(self):
        return f'Q:{self.state},{self.action}'