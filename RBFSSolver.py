import pycuber
# TODO: recursive BFS for solving the rubiks cube


# start - a state of the cube
# successors - a function that calculates the successors of a state
# state_value - a function that calculates the heuristics of a state
# is_goal - a function that calculates whether a state is the goal
# f_limit - just an f-limit
def rbfs_search(start, successors, state_value, is_goal, f_limit):
    if is_goal(start):
        return [start, 0]
    g = 1
    h = state_value(start)
    f = g + h
    # get successors from start state
    # if successors is empty, return failure and arbitrarily large f-limit
    if not successors:
        return [-1, 999999]

    # for each s in successors
        # update f with value from previous search
        # s.f <-- max(s.g + s.h, node.f)
    # loop do
        # best <-- lowest f-value in successors
        # if best.f > f-limit, return [failure, best.f]
        # alternative <-- second lowest f-value among successors
        # result, best.f <-- RBFS(start, successors, state_value,
        # if result != failure, return result


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