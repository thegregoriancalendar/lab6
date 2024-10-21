# Gregory Roudenko

password = ""
quit = False

def encode(string):
    global password
    # loops through chars in string
    for i in range(len(string)):
        newVal = int(string[i]) + 3
        # wraparound check
        if newVal >= 10:
            newVal -= 10
        # changes the char
        string = string[:i] + str(newVal) + string[i + 1:]
    password = string
    print("Your password has been encoded and stored!")

    return string


def decode(encoded):
    decoded = "" # initialize empty string for result to be returned
    # Loops through each digit in the encoded password, changes it to an integer, and subtracts 3. If the new digit is
    # less than 0, adds 10 to account for encoded values that would have been greater than 10 when increased by 3. Each
    # new digit is then changed to a string and added to the decoded string, which is returned when completed.
    for digit in encoded:
        temp_digit = int(digit) - 3
        if temp_digit < 0:
            temp_digit += 10
        decoded += str(temp_digit)
    print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        
def main():
    choice = input("Choose a function (encode or decode) or enter \"quit\" to quit: ")
    if choice == "quit":
        return True
    val = input("Choose a value to " + choice + ": ")
    # evaluates whatever function you enter into the prompt
    #stores encoded password in global password variable
    eval(choice + "(\"" + val + "\")")
    

# loop
if __name__ == "__main__":
    while (not quit):
        quit = main()