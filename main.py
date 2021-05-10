import pycuber as pc
from pycuber.solver import CFOPSolver

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a Cube object
    mycube = pc.Cube()

    #random algorithm
    random = pc.Formula().random()

    # Do something at the cube.
    mycube(random)

    print(mycube)