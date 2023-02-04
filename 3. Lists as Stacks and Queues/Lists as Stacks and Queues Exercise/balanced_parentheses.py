from collections import deque


the_string = input() # takes in the input to check
my_stack = deque() # creates an empty queue


def matches(open,close):
    '''Checks whether the respective opening and closing parentheses match'''
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

def parChecker(input_string):
    '''Checks whether a string of parentheses are all strings balanced'''
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        symbol = input_string[index] # takes in respective symbol in string starting from index 0
        if symbol in '{[(':
            my_stack.append(symbol)
        else:
            if len(my_stack) == 0:
                balanced = False
            else:
                top = my_stack.pop()
                if not matches(top, symbol):
                    balanced = False
                
        index += 1

    if balanced and len(my_stack) == 0:
        return 'YES'
    else:
        return 'NO'

print(parChecker(the_string))