import pycuber
import sys

def createTestFile(size):
    for i in range(0, size):
        filename = "test" + str(i)
        randomFormula = str(pycuber.Formula().random())
        # print(randomFormula)
        with open(filename, "w") as writer:
            writer.write(randomFormula)
    
if __name__ == "__main__":
    number = int(sys.argv[1])
    createTestFile(number)