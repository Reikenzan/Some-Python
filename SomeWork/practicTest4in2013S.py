# Write a function that takes as two parameters: the name of a country
# (one of Japan, Indonesia, or Hungary) and an amount of U.S. currency.
# Your function should convert the amount of U.S. dollars into the currency
# of the given country. If the country passed to the function is not on the
# list, return -1. The conversion rates for these countries are $1 US = 83.85
# Japanese Yen, 9639.99 Indonesian Rupiahs, and 0.00456 Hungarian Forints.
""" #My code
inDollar = int()

def currency(name,dollars):    
    
    if (name == "Japan"):
        inDollar = dollars * 83.85
    elif (name == "Indonesia"):
        inDollar = dollars * 9639.99
    elif (name == "Hungary"):
        inDollar = dollars * 0.00456
    else:
        print("None in database")
    return inDollar

def main():
    nameC = str(input("Which country are you travelling to: "))
    dollar = float(input("Enter the amount of US dollars to convert: "))

    conver = currency(nameC, dollar)

    print("In ",nameC,"you have", conver,"of their currency.")

if __name__ == "__main__":
    main()"""

#Prof.'s code
def convertCurrency(countyName, us):
    if countyName == "Japan":
        convertedAmount = us * 83.85
    elif countyName == "Indonesia":
        convertedAmount = us * 9639.99
    elif countyName == "Hungary":
        convertedAmount = us * 0.00456
    else: #defualt case if no one of the above
        convertedAmount = -1
    return convertedAmount

def main():
    usd = float(input("Enter the amount of US dollars to convert: "))
    country = (input("Which country are you travelling to: "))

    amount = convertCurrency(country,usd)

    print("In ",country,"you have",amount,"of their currency.")

if __name__ == "__main__":
    main()
