"""Write a program that reads in a text file, infile.txt and writes to an
output file, outfile.txt. Your program should write all the lines in
infile.txt that have more than 15 characters to outfile.txt in all upper case."""

fileref = open("infile.txt",'r')

outfile = open("outfile.txt",'w')

for line in fileref:
    if len(line) > 15:
        outfile.write(line)

fileref.close()
outfile.close()
