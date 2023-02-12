num = int(input())
matrix = []

for x in range(num):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)

# new_matrix = [el for row in matrix for el in row] 
new_matrix = []
for row in matrix:
    for el in row:
        new_matrix.append(el)
print(new_matrix)