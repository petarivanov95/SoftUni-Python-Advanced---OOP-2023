my_input = input()

# create a list to store the indexes of '(' characters
indexes = []

# loop through the input string
for id, ch in enumerate(my_input):
    ch = my_input[id]
    
    # if the character is '(', add its index to the 'indexes' list
    if ch == '(':
        indexes.append(id)
        
    # if the character is ')', remove the most recently added index from the 'indexes' list and print the substring between that index and the current index
    elif ch ==')':
        opening_index = indexes.pop()
        print(my_input[opening_index:id+1])



## Sanople input
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

