## Method #1 - using lists

# my_input = list(input()) # takes in the input and makes it into a list

# while len(my_input) > 0: # with each iteration check the list length
#     print(my_input.pop(),end='') # pop the last item

## Method #2 - using collections library
from collections import deque

stack = deque()

my_input = input()

for x in my_input:
    stack.append(x)

while len(stack) > 0:
    print(stack.pop(),end='')