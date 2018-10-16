"""(a) Write a complete class that keeps tracks of information
about chocolate. Your class, Chocolate should contain instance
variables for the name, pricePerPound, weight and countryOfOrigin,
and should have a constructor method as well as a method, cost(),
that returns the price (pricePerPound * weight) for the chocolate
and a method, getWeight(), that returns theweight for the chocolate.

(b)Write a function that takes as input a list of chocolate, called
shoppingList, and returns the most expensive chocolate in the list
(i.e. the maximum of all the costs of the chocolate in the inputted list):
    def maxWeight(shoppingList):
"""
# (a)
class Chocolate:
    # constructor
    def __init__(self, initName,initPrice,initWeight,initCountry):
        self.name = initName        
        self.weight = initWeight
        self.price = initPrice
        self.countryOfOrigin = initCountry
    # getter
    def getWeight(self):
        return self.weight

    def cost(self):
        return self.price * self.weight

    def __str__(self):
        return self.name + ", $" + str(self.cost())

# (b)

def maxCost(shoppingList):
    mostExpensiveSoFar = shoppingList[0]
    for choc in shoppingList:
        if choc.cost() > mostExpensiveSoFar.cost():
            mostExpensiveSoFar = choc
        #print(choc.cost())
    return mostExpensiveSoFar
        


choc1 = Chocolate("Choc1",0.5,2,"Peru")
choc2 = Chocolate("Choc2",0.1,5,"Columbia")
choc3 = Chocolate("Choc3",1,1,"Ecuador")

chocList = [choc1,choc2,choc3]
print(maxCost(chocList))
