# want to find all players 30 or older


# open NBA data file
infile = open("nba_2013.csv",'r')

# skip first line(col heading) using reasdline()
infile.readline()

# loop throu rest of file
for line in infile:
    # split line to put col entries in a list
    linelist = line.split(",")
    # get age at position 2 in list
    age = int(linelist[2])
    
    # if age is >= 30
    if age >= 30:
        # print out that player's line
        print(line)

#print out each line
for line in infile:
    print(line)
