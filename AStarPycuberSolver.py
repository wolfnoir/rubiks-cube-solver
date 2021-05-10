# TODO: retrieving the number of explored state from pycuber's A* implementation

"""
NOTE: a_star_search, path_states, path_actions METHODS ARE TAKEN DIRECTLY FROM PYCUBER AND IS NOT ORIGINAL
Modifications are made to A* to retrieve the number of states explored
"""

class a_star():

    def __init__(self):
        self.explored = list()

    def a_star_search(start, successors, state_value, is_goal):
        """
        This is a searching function of A*.
        THIS CODE IS NOT ORIGINAL. SLIGHT MODIFICATIONS WERE MADE TO GET THE EXPLORED STATES
        """
        if is_goal(start):
            return [start]
        explored = []
        g = 1
        h = state_value(start)
        f = g + h
        p = [start]
        frontier = [(f, g, h, p)]
        while frontier:
            f, g, h, path = frontier.pop(0)
            s = path[-1]
            for (action, state) in successors(s, path_actions(path)[-1] if len(path) != 1 else []):
                if state not in explored:
                    path2 = path + [action, state]
                    h2 = state_value(state)
                    g2 = g + 1
                    f2 = h2 + g2
                    if is_goal(state):
                        self.explored = explored
                        return path2
                    else:
                        frontier.append((f2, g2, h2, path2))
                        frontier.sort(key=lambda x:x[:3])
        self.explored = explored
        return []
    
    def path_states(path):
        """
        Return a list of states in this path.
        THIS CODE IS NOT ORIGINAL.
        """
        return path[0::2]
    
    def path_actions(path):
        """Return a list of actions in this path.
        THIS CODE IS NOT ORIGINAL.
        """
        return path[1::2]