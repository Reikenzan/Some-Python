s = "Football*Basketball*Hockey*Baseball*Soccer"
num = s.count("*") + 1
sports = s.split("*")
print("There are", num, "sports")
print("Two of them are",sports[0], sports[-2])
mess = "Poaoxci BnletRc caGnqu oaUxr Fd"
result = ""
for i in range(len(mess)):
    if i % 3 == 0:
        print(mess[i])
        result = result + mess[i]
print(sports[1], result)
