
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.wind_strength = None

        self.is_terminal = self.find_if_terminal()

    def find_if_terminal(self):
        return self.x == 7 and self.y == 3

    def __repr__(self):
        return f'Cell at ({self.x},{self.y})'