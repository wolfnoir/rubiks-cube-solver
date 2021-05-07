# TODO: bidirectional search for solving the rubiks cube
from util import cNode

class BDS():

    def __init__(self):
        self.explored = list()

    def BFS(self, startNode):
        frontier = list()
        goal = False
        if goal: # perform goal check
            return startNode
        frontier.append(startNode)
        while frontier != []: 
            currentNode = frontier.pop(0)
            self.explored.append(currentNode)
            for action in currentNode.actions:
                newNode = None # create new rubix cube
                if newNode not in frontier and newNode not in self.explored: # check if value of the rubix cube is the same
                    if goal: # perform goal check
                        return newNode
                    frontier.append(newNode)

