
def getNumTrips(balance):
    balance = balance // 2.75
    

def main():
    bal = float(input("Enter your Metrocard balance:"))
    numTrips = getNumTrips(bal)
    print("You can take", numTrips ,"more trips on the subway.")

if _name_ == "_main_":
    main()
