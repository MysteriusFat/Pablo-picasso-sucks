import random as rd
class Polygon():
    def __init__(self, color, vectors):
        self.color = color
        self.vectors = vectors
        self.mutate_ratio = 0.5


    def mutate(self, size):
        if rd.random() <= self.mutate_ratio:
            self.color = (rd.randrange(0,256),rd.randrange(0,256),rd.randrange(0,256),rd.randrange(0,256))
        else:
            index = rd.randrange(0, len(self.vectors))
            self.vectors[index] = (rd.randrange(0, size[0]),rd.randrange(0, size[1]))
