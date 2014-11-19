# EZ hack@metahack.com
# Code 

class Balance():

    def __init__(self):
        self.delimiters = [ ['(', ')'], ['{', '}'] ]
        self.openers = []
        self.closers = []

        for i in self.delimiters:
            self.openers.append(i[0])
            self.closers.append(i[1])

        print(self.openers, self.closers)
        
    
    def match(self, input_string):
        stack = []

        for symbol in input_string:
            for i in self.delimiters:
                if symbol in self.openers:
                    stack.append(symbol)

                if symbol in self.closers:
                    if len(stack) == 0:
                        return False

                    else:
                        if self.openers.index(stack.pop()) != self.closers.index(symbol):
                            return False


        if len(stack) > 0:
            return False

        return True
                
    """
        left_count = 0
        right_count = 0

        for i in input_string:
            if i == self.left:
                left_count += 1

            if i == self.right:
                right_count +=1

            if right_count > left_count:
                return False


        if left_count != right_count:
            return False
                    
        else:
            return True
        """



# START OF STANDALONE TESTS #

def main():
    import sys

    parens = Balance()


    if len(sys.argv) < 2:
        print("Argument required for command-line use; running default tests.")

        test_passing_lists = [
            list("(()()()())"),
            list("(((())))"),
            list("(()((())()))") ]

        test_failing_lists = [
            list("((((((())"),
            list("()))"),
            list("(()()(())") ]

        for i in test_passing_lists:
            assert parens.match(i), "\n{}\nfailed in error".format(i)

        for i in test_failing_lists:
            assert not parens.match(i), "\n{}\npassed in error".format(i)

        print("tests passed")


    else:
        list_to_check = sys.argv[1]

        print(parens.match(list_to_check))


if __name__ == "__main__":
    main()

