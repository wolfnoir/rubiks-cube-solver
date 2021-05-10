# TODO: bidirectional search for solving the rubiks cube
import pycuber as pc
from util import cNode
import copy

class BDS():

    def __init__(self):
        self.explored = list()
        self.intersectionNode = None

    def BDSSolver(self, startNode, endNode):
        if startNode.cube == endNode.cube: # initial check if the start state is the goal state
            return startNode
        frontier = [startNode, endNode]
        while frontier != []: 
            currentNode = frontier.pop(0)
            self.explored.append(currentNode)
            for action in currentNode.actions: # for each avaliable action create a new node with that state
                newNode = self.createNewNode(currentNode, action)
                if not self.checkStateExists(newNode, frontier) and not self.checkStateExists(newNode, self.explored): # if cube state doesnt exist added it to frontier
                    frontier.append(newNode)
                else: # if cube state exists in frontier or explored 
                    cubeNode = self.getExistingCube(newNode, frontier)
                    if cubeNode != None and cubeNode.direction != currentNode.direction: # if the directions are not the same, then an intersection has been reached
                        cubeNode.intersection = newNode
                        self.intersectionNode = cubeNode
                        return cubeNode
    
    def createNewNode(self, rubikCube, action):
        formula = rubikCube.formula + " " + action
        cubeFormula = pc.Formula(formula)
        cube = pc.Cube()
        cube(cubeFormula)
        node = cNode(cube, formula) # create node with rubik cube state
        node.parent = rubikCube # get parent
        node.action = action # get action taken
        self.removeActions(node, action) # remove action taken from available actions 
        node.direction = rubikCube.direction # set direction 
        return node

    def removeActions(self, node, action):
        # removes action taken from available actions
        if "'" in action:
            node.actions.remove(action[:-1]) # removes last char
        else:
            node.actions.remove(action+"'")
    
    def checkStateExists(self, node, cubeNodes):
        # checks if rubik cube state exists in a list of cNodes
        for cubeNode in cubeNodes:
            if node.cube == cubeNode.cube:
                return True
        return False
    
    def getExistingCube(self, node, cubeNodes):
        # returns a node with the existing rubik cube state
        for cubeNode1 in cubeNodes:
            if node.cube == cubeNode1.cube:
                return cubeNode1
        for cubeNode2 in self.explored:
            if node.cube == cubeNode2.cube:
                return cubeNode2
        return None
    
    def getActionsTaken(self):
        actionsTaken = []
        parentNode = self.intersectionNode
        while parentNode.parent != None:
            if parentNode.direction == 0:
                actionsTaken.append(parentNode.action)
            else:
                if "'" in parentNode.action:
                    actionsTaken.append(parentNode.action[:-1])
                else:
                    actionsTaken.append(parentNode.action+"'")
            parentNode = parentNode.parent
        intersectNode = self.intersectionNode.intersection
        while intersectNode.parent != None:
            if intersectNode.direction == 0:
                actionsTaken.append(intersectNode.action)
            else:
                if "'" in intersectNode.action:
                    actionsTaken.append(intersectNode.action[:-1])
                else:
                    actionsTaken.append(intersectNode.action+"'")
            intersectNode = intersectNode.parent
        return actionsTaken

if __name__ == "__main__":
    goalCube = pc.Cube() # create goal Node
    goalFormula = ""
    goalAlg = pc.Formula(goalFormula)
    randomCube = pc.Cube() # create start Node
    randomFormula = "U R"
    randomAlg = pc.Formula(randomFormula)
    # randAlg = alg.random()
    randomCube(randomAlg)
    startNode = cNode(randomCube, randomFormula)
    endNode = cNode(goalCube, goalFormula)
    endNode.direction = 1
    BiDirectionalSolver = BDS()
    goal = BiDirectionalSolver.BDSSolver(startNode, endNode)
    actionsTaken = BiDirectionalSolver.getActionsTaken()
    print(actionsTaken)