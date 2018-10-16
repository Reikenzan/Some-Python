# convert Celcious to Farenheit

def tempConvert(Celcius):
    Farenheit = Celcius * (9/5) + 32
    return Farenheit

#print("The temperature in Farenheit is", F)

def main():
    C = float(input("Enter a temp:"))
    F = tempConvert(C)
    print("In Farenheit:",F)

if _name_ == "_main_":
    main()
