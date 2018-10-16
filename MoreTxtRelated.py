"""
fileref = open("myFile.txt",'r')
for line in fileref:
    print(line) # or print("***"+line.strip())
fileref.close()
"""
fileref = open("myFile.txt",'r')
outfile = open("myOutfile.txt",'w')
for line in fileref:
    s= "***"+line.strip()
    print(s)
    outfile.write(s + "\n")
fileref.close()
outfile.close()




