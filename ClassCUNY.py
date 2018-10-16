""" Write a Class that sotres info about a CUNY School:
    - name
    - # of undergrad
    - # of grad students
Write a constructor, getNumUndergrads(), setNumUndergrads(),
and a method called totalStudents() that returns the total #
of students(both under and grad) at the school"""


class CUNY:
    # constructor
    def __init__(self, initName,initNumUndergrads, initNumGrads):
        self.name = initName
        self.NumUndergrads = initNumUndergrads
        self.NumGrads = initNumGrads
    #getter
   # def getName(self):
   #     return self.name

    def getNumUndergrads(self):
        return self.NumUndergrads
    #setter
    def setNumUndergrads(self, newNum):
        self.NumUndergrads = newNum
    
    def totalStudents(self):
        total = self.NumUndergrads + self.NumGrads
        return total


def main():
    lehman= CUNY("Lehman",10000,500)
    print("The number of undergrads is:",lehman.getNumUndergrads())
    lehman.setNumUndergrads(12000)
    print("The number of undergrads is:",lehman.getNumUndergrads())
    total = lehman.totalStudents()
    print("Total students =",total)

    queens = CUNY("Queens",15000,1000)
    print("Total students at Queens =",queens.totalStudents())
    print("Total students at Lehman=",total)
if __name__ == "__main__":
    main()
