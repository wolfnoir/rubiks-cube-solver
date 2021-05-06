import pycuber


# TODO: recursive BFS for solving the rubiks cube

def rbfs_search(start, successors, state_value, is_goal):
    if is_goal(start):
        return [start]
    g = 1
    h = state_value(start)
    f = g + h

    return


class RBFSSolver(object):
    # takes in a pycuber cube as a parameter
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        if not self.cube.is_valid():
            raise ValueError("Invalid Cube.")
        # saves the result of the algo
        result = pycuber.Formula()


class RBFSCross(object):
    def __init__(self, cube):
        self.cube = cube