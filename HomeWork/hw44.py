"""Write a program that asks the user for the name of an input file and
the name of an output file. Your program should replace all occurrences
of "NY" in the input file text with "New York", all occurrences of "NJ"
with "New Jersey", and all occurrences of "CT" with "Connecticut" and
write the results to the output file."""

filename = input("Enter a file name: ")
openfile = open(filename, 'r')
readfile = openfile.read()

Replace = readfile.replace("NJ", "New Jersey")
Replace = Replace.replace("NY", "New York")
Replace = Replace.replace("CT","Connecticut")

print(Replace)
    
openfile.close()
