quit = False

def encode(string):
    for i in range(len(string)):
        newVal = int(string[i]) + 3
        if newVal >= 10:
            newVal -= 10
        string = string[:i] + str(newVal) + string[i + 1:]
    return string
        
def main():
    choice = input("Choose a function (encode or decode) or enter 'quit' to quit: ")
    if choice == "quit":
        return True
    val = input("Choose a value to " + choice + ": ")
    print(eval(choice + "(\"" + val + "\")"))


if __name__ == "__main__":
    while (not quit):
        quit = main()