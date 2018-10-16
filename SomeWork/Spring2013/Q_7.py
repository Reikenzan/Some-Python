"""Write a program that reads in a text file, infile.txt, and prints out the line numbers of the lines
containing the word Python in the file."""
infile = open("infile.txt",'r')

lineNum = 1
for line in infile:
    if line.find("Python")>-1:
        print(lineNum)
    lineNum = lineNum +1


