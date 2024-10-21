# Gregory Roudenko

quit = False

def encode(string):
    # loops through chars in string
    for i in range(len(string)):
        newVal = int(string[i]) + 3
        # wraparound check
        if newVal >= 10:
            newVal -= 10
        # changes the char
        string = string[:i] + str(newVal) + string[i + 1:]
    return string
        
def main():
    choice = input("Choose a function (encode or decode) or enter \"quit\" to quit: ")
    if choice == "quit":
        return True
    val = input("Choose a value to " + choice + ": ")
    # evaluates whatever function you enter into the prompt
    print(eval(choice + "(\"" + val + "\")"))

# loop
if __name__ == "__main__":
    while (not quit):
        quit = main()