"""Write a complete class that keeps tracks of information about train
lines. Your class, TrainLine should contain instance variables for the
name, length, dailyRidership and coverageArea, and should have:
    -a constructor method,
    -a method, getLength(), that returns the train length a method, and
    -a method, riderDensity() that calculates rider density ("dailyRidership/
    coverageArea")
Outside of your class, write a function that takes as input a list of
TrainLines, called subway, and returns the sum of the length of the train
lines in the list. The function signature should be:
		def overallLength(subway):	
Include a main() in your file that demostrates that your class and function
work. This homework will be graded manually, so there are no test cases."""

class TrainLine:
    # constructor
    def __init__(self, initName,initLenght,initDailyRidership,initCoverageArea):
        self.name = initName
        self.length = initLenght
        self.dailyRidership = initDailyRidership
        self.coverageArea = initCoverageArea
    
    def getName(self):
        return self.name

    def getLength(self):
        return self.length

    def riderDensity(self):
        return self.dailyRidership / self.coverageArea

def overallLength(subway):
    #suma = 0
    """
    for line in trainLines:
    for num in line.split(','):
        suma = suma + int(num.strip())
        """
    #n=str(n)
    numbers=[]
    for num in subway:
        numbers.append(int(x))
    return sum(numbers)

        
def main():
    metroN = ("Metro North",15,20,5)
    metroN.getLength()
    print(metroN)
    totalL = overallLength()
    print("The sum of the length is:", totalL)
main()

