# to make a class:

class City:
    # make the constructor which creates a City object
    #(ie. sets up all the instance vars)
    def __init__(self, initName,initPop,initArea):
        self.name = initName
        self.population = initPop
        self.area = initArea
#getters: return instance variables
    def getName(self):
        return self.name
    
    def getPop(self):
        return self.population
    
    def getArea(self):
        return self.area
#setters: change instance variables
    def setPop(self, newPop):
        self.population = newPop
    
    def calculateDensity(self):
        return self.population/self.area

newYork = City("New York", 8500000,470)
print(newYork)
print(newYork.getName())
print(newYork.getPop())
print(newYork.getArea())
newYork.setPop(8600000)
print("new pop:",newYork.getPop())
print(newYork.calculateDensity())


mad = City("Madrid",3141991,604)
print(mad)
print(mad.getName())
print(mad.getPop())
print(mad.getArea())
print(mad.calculateDensity())
