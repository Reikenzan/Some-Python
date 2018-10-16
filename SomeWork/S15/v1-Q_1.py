s = "Ada=>Lovelace=>Charles=>Babbage"
a = s[0:3]
print(a.upper())
names = s.split("=>")
print(names)
b,c,d = names[1],names[2],names[3]
print(c,d)
print(b[-1]+"n"+d[-2]+"ine")
print('Put_line: ("', a.lower(),'")')
