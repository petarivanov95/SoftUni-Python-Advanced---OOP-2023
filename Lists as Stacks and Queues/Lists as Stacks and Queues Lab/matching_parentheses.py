my_input = input()

indexes = []

for i in range(len(my_input)):
    ch = my_input[i]
    if ch == '(':
        indexes.append(i)
    elif ch ==')':
        opening_index = indexes.pop()
        print(my_input[opening_index:i+1])



# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

