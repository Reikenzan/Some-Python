"""Make a class called Dog, that stores the name and age of the dog as
instance var. write methods getAge() & setAge(), getAgeInHumanYears()"""

class Dog:
    def __init__(self, initName,newAge):
        self.name = initName
        self.age = newAge

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setAge(self, newAge):
        self.age = newAge

    def getAgeInHumanYears(self):
        return self.age*7

    def __str__(self):
        return self.name + "(" + str(self.age) + ")"
        #return self.name + "(" + str(self.getAgeInHumanYears()) + ")"


def sumAges(listOfDogs):
    total = 0
    for dog in listOfDogs:
        total = total + dog.getAge()
    return total


def main():
    fido = Dog("Fido", 5)
    print("The age is:",fido.getAge())
    humanAge = fido.getAgeInHumanYears()
    print("In human years:",humanAge)
    fido.setAge(6)
    print("The new age is:",fido.getAge())
    humanAge = fido.getAgeInHumanYears()
    print("In human years:",humanAge)

    spot = Dog("Spot",1)
    whiskers =Dog("Whiskers",11)

    dogList = [fido,spot,whiskers]
    for dog in dogList:
        print(dog)
    print("Ages of all dogs = ", sumAges(dogList))
if __name__ == "__main__":
    main()
