#open file for writing
outfile = open("myfile.txt",'w')

outfile.write("Hello!\n")
outfile.write("I am writing to my file.\n")
outfile.write("Isn't this cool?\n")

for i in range(1,11):
    outfile.write(str(i)+"\n")

outfile.close()
