

class Move:
    def __init__(self):
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0
        pass

    def __rotate_m1(self, degrees):
        self.m1 += degrees
        pass

    def __rotate_m2(self, degrees):
        self.m2 += degrees
        pass

    def __rotate_m3(self, degrees):
        self.m3 += degrees
        self.__rotate_m2(degrees)
        pass

    def to(self, x, y, z):
        pass

