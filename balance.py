


class Balance():

    def __init__(self):
        pass
    
    def go(input_string):
        return("Finally... {}!!!".format(input_string))


# START OF STANDALONE TESTS #

if __name__ != "__main__":
    exit()

import sys

if len(sys.argv) < 2:
    print("error: argument required")
    sys.exit()

string_to_check = ""


print(sys.argv[1])

print(Balance.go("It's happening..."))

print("If Balance is a module, I shouldn't exist.")