#     A program to convert a textual message into a Caesar cipher

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")
    
    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    for ch in message.upper():
        index = (ord(ch) - ord('A')+1) %26
        print(chr(ord('A')+index), end=" ")    
        
    print() # blank line before prompt

main()
