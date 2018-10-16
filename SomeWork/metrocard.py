balance = float(input("What is your starting metrocardbalance?"))
numTrips = int(input("How many trips did you make?"))
balance = balance - numTrips * 2.75
added = float(input("How much money did you add?"))
balance = balance + added
print("Your current balance is "+ str(balance))
