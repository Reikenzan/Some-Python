"""Write a program that asks the user for a file containing a
(different) program and a name for an output file. Your program
should then write the program, with line numbers to the output
file. For example, if the input file is:
def main():
	for i in range(10):
		print("I love python")
	print("Good bye!")
Then the output file would be:
1	 def main():
2		for i in range(10):
3			print("I love python")
4		print("Good bye!")
Hint: to preserve the spacing, also write a TAB ('\t') after the
number on each line."""


filename = input("Please enter a file name: ")
filename2 = input("Please enter a file name to save the output: ")

openfile = open(filename, "r")
readfile = openfile.readlines()

out_file = open(filename2, "w")

for i , line in enumerate(readfile):
    out_file.write("%d \t %s" %(i+1, line))
    

out_file.close()
