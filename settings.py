class Settings:
    """ Class definition for General Settings of the program"""
    def __init__(self):
        self.screen_width   = 240
        self.screen_height  = 360
        self.caption        = "Maze Solver"
        self.bg_color       = [0, 0, 0]
        self.FPS            = 120

        self.boundary_limit = 10
        self.boundary = {
            'top'   : self.boundary_limit,
            'right' : self.screen_width - self.boundary_limit,
            'bottom': self.screen_height - self.boundary_limit,
            'left'  : self.boundary_limit
        }

    def screen_size(self):
        """ Returns the screen size as a tuple """
        return (self.screen_width, self.screen_height)