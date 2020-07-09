import pygame as py

class Display:
    def __init__(self):
        py.init()
        self.pixel_length = 100
        self.size = (10*self.pixel_length,7*self.pixel_length)

        self.display_window = py.display.set_mode((self.size))
        self.background = py.Surface(self.display_window.get_size()).convert()
        self.background.fill((128, 0, 128))

        self.boat_image = Boat_Image(self.pixel_length)
        self.terminal = Terminal(self.pixel_length)

    def update_screen(self,boat):
        boat_x, boat_y = boat.coord
        boat_x, boat_y = self.pixel_length*boat_x, self.pixel_length*boat_y
        
        term_x,term_y = 7*self.pixel_length,3*self.pixel_length

        self.display_window.blit(self.background,(0,0))
        self.display_window.blit(self.boat_image.image,(boat_x,boat_y))
        self.display_window.blit(self.terminal.image,(term_x,term_y))

        py.display.flip()

    def check_if_exit(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = False
                py.quit()  
                return True

class Boat_Image:
    def __init__(self,pixel_length):
        self.side_length = pixel_length
        self.image = py.Surface((self.side_length,self.side_length)).convert()
        self.colour = (255,165,0)

        self.fill_in()
    
    def fill_in(self):
        self.image.fill(self.colour)

class Terminal(Boat_Image):
    def __init__(self,pixel_length):
        super().__init__(pixel_length)
        self.colour = (255, 192, 203)
        self.fill_in()

if __name__ == "__main__":
    disp = Display()

