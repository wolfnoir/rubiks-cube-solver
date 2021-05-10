import pycuber as pc
import datetime
from RBFSSolver import RBFSSolver
import os

if __name__ == '__main__':
    # keeps track of the number of files read to calculate the average
    num = 0
    # keep track of number of states explored
    total_states = 0
    total_depth = 0
    #while mode != 1 or mode != 2 or mode != 3:
    mode = input("Pick which algorithm to run:\n"
                "1) A* \n"
                "2) Recursive BFS \n"
                "3) Bidirectional Search\n")
    # start time
    start = datetime.datetime.now()

    for filename in os.listdir("TestFiles"):
        num += 1
        file = open("TestFiles/" + filename)
        file_contents = file.read()
        file.close()
        formula = pc.Formula(file_contents)
        cube = pc.Cube()
        cube(formula)
        # insert appropriate solving algorithm below
        if mode == "1":
            print("A*")
        elif mode == "2":
            solver = RBFSSolver(cube)
            result = solver.solve()
            total_states += result[1]
            total_depth += len(result[0])
        elif mode == "3":
            print("Bidirectional Search")

    time_diff = datetime.datetime.now() - start
    execution_time = time_diff.total_seconds() * 1000
    # calculate the average time of execution
    avg_time = execution_time / num
    # calculate the average depth of solution
    avg_depth = total_depth / num
    # calculate the average number of states explored
    avg_states = total_states / num
    print(f"Average Time: {avg_time} ms")
    print(f"Average Depth of Solution: {avg_depth}")
    print(f"Average States Explored: {avg_states}")
