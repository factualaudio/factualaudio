from math import sqrt

def distance(xy1, xy2):
    return sqrt(sum([(dim[0]-dim[1])**2 for dim in zip(xy1, xy2)]))

def midpoint(xy1, xy2):
    return [sum(dim) / len(dim) for dim in zip(xy1, xy2)]
