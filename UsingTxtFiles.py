"""Open file(from pc) and initialize fileref as
variable for accessing the file"""

fileref = open("enrollment.txt",'r')

for line in fileref:
    print(line.strip())#use strip to remove newline
    print(line, end = "")#print not to add a list
    print(line[:-1])#remove last char
fileref.close()

fileref = open("enrollment.txt",'r')
total =0
for line in fileref:
    li = line.split()
    total = total + int(li[1])
print("Total CUNY students:", total)
fileref.close()
