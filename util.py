class cNode():
    """
    Parameters:
        cube: current state of the rubix cube
        prev: previous node with previous rubix cube state
        next: next node with previous rubix cube state
        actions: a list of available actions to take
    """
    def __init__(self, cube):
        self.cube = cube
        self.prev = None
        self.next = None
        self.actions = []