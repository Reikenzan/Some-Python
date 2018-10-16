""" Given the following program and input, what is printed:
Cana
San
San
Plata
Domingo
"""

def main():
    infile = open("infile.txt", "r")
    for line in infile:
        index = line.find(" ")
        if line.find("de") > -1:
            print( line[:index] )
        else:
            print( line[index+1:], end="" )
main()
