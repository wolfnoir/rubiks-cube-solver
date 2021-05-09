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
    # change g to be dynamic....this is not correcet
    g = 1
    h = state_value(start)
    f = g + h
    # get successors from start state
    successors_stuff = successors(start, [])
    # if successors is empty, return failure and arbitrarily large f-limit
    if not successors:
        return [-1, 999999]
    successors_f_values = []
    i = 0
    # for each s in successors
    for (action, state) in successors_stuff:
        print(state)
        new_f = state_value(state) + 1
        max_f = max(new_f, f)
        temp = (max_f, i)
        successors_f_values.append(temp)

    while True:
        # sort successors by f-value
        sorted(successors_f_values, key=lambda successor: successor[0])
        # best <-- lowest f-value in successors
        best = successors_f_values[0]
        successor_index = best[1]
        if best[0] > f_limit:
            return [-1, best[0]]
        # alternative <-- second lowest f-value among successors
        alternative = successors_f_values[1]
        # result, best.f <-- CALL RBFS HERE
        result = 0
        # if result != failure, return result
        if result[0] != -1:
            return result


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