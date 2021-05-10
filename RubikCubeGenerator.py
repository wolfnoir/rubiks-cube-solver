import pycuber
import sys

def createTestFile(size):
    for i in range(0, size):
        filename = "test" + str(i)
        randomFormula = str(pycuber.Formula().random())
        with open(filename, "w") as writer:
            writer.write(randomFormula)
    
def createTestFile5(size):
    for i in range(0, size):
        filename = "test" + str(i)
        randomFormula = str(pycuber.Formula().random())
        formulaArr = randomFormula.split(" ")[:5]
        randomFormula = " ".join(formulaArr)
        with open(filename, "w") as writer:
            writer.write(randomFormula)

def createTestFile3(size):
    for i in range(0, size):
        filename = "test" + str(i)
        randomFormula = str(pycuber.Formula().random())
        formulaArr = randomFormula.split(" ")[:3]
        randomFormula = " ".join(formulaArr)
        with open(filename, "w") as writer:
            writer.write(randomFormula)

if __name__ == "__main__":
    number = int(sys.argv[1])
    createTestFile3(number)
