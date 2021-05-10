class cNode():
    """
    Parameters:
        cube: current state of the rubix cube
        parent: previous node with previous rubix cube state
        intersection: next node with previous rubix cube state
        direction (For BidirectionalSearch): 0 = front-to-back, 1 = back-to-front
        actions: a list of available actions to take
    """
    def __init__(self, cube, formula):
        self.cube = cube
        self.parent = None
        self.formula = formula
        self.intersection = None
        self.direction = 0 
        self.action = None
        self.actions = ["F", "R", "U", "L", "B", "D", "M", "E", "S", "F'", "R'", "U'", "L'", "B'", "D'", "M'", "E'", "S'"]