import pycuber as pc
import datetime
import os

if __name__ == '__main__':
    # keeps track of the number of files read to calculate the average
    num = 0
    # start time
    start = datetime.datetime.now()

    for filename in os.listdir("TestFiles"):
        num += 1
        file = open("TestFiles/" + filename)
        input = file.read()
        file.close()
        formula = pc.Formula(input)
        cube = pc.Cube()
        cube(formula)
        # insert appropriate solving algorithm below

    time_diff = datetime.datetime.now() - start
    execution_time = time_diff.total_seconds() * 1000
    # calculate the average time of execution
    avg_time = execution_time / num
    # calculate the average depth of solution
    # calculate the average number of states explored
