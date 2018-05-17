class Path:

    def __init__(self, path):
        self.path = path
        self.i = 0

    def next(self):
        coord = self.path[self.i]
        self.i += 1