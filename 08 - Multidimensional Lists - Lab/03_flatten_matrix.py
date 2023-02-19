num = int(input())
matrix = []

# loop through range num and get row data
for x in range(num):
    # get input as string and split by comma and space
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)

# flatten the matrix list and store in new_matrix
new_matrix = []
for row in matrix:
    for el in row:
        new_matrix.append(el)

# print the new_matrix list
print(new_matrix)
