"""Given the following program and input file, what is printed:
Output:
SAMBA, BRAZIL
CUMBIA, COLOMBIA
SYRTAKI, GREECE
Hip-hop
"""
def sixV1():
    infile=open("music.txt","r")
    for line in infile.readlines():
        if len(line)>8:
            print(line.upper())
        else:
            print(line)
sixV1()
