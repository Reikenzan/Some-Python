# ask user for a word
word = input("Enter a word(hit 'enter' to finish): ")

# create an empty list called word_list
word_list = []

#while word no empty, user enters a word
while word != "":
    # add word to lis
    word_list.append(word) #kind of like: word_list = word_list + word
    print("word_list so far:",word_list)
    # ask for another word
    word = input("Enter a word(hit 'enter' to finish): ")

print("All done!")
