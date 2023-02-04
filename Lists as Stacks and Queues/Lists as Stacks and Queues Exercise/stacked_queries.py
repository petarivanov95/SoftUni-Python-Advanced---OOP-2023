from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]), # push the number onto the stack; index 1 for list position, not zero 
    2: lambda x: numbers.pop() if numbers else None, # delete number from top of stack
    3: lambda x: print(max(numbers)) if numbers else None, # prints max of stack
    4: lambda x: print(min(numbers)) if numbers else None, # prints min of stack
}

for _ in range(int(input())):
    input_data = [int(x) for x in input().split()] # the input gets split could be 1 or 2 elements
    map_functions[input_data[0]](input_data) # calls the dictionary function but also need to pass it an argument in the parenthesis

numbers.reverse()

print(*numbers, sep=", ") # the * is used for unpacking
