
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.wind_strength = self.calc_wind()

        self.is_terminal = self.find_if_terminal()

    def calc_wind(self):
        if self.x >= 3 and self.x <=5:
            return 1
        elif self.x == 6 or self.x == 7:
            return 2
        elif self.x == 8:
            return 1
        else:
            return 0

    def find_if_terminal(self):
        return self.x == 7 and self.y == 3