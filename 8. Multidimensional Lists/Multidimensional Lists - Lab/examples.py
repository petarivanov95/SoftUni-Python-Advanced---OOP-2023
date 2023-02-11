rows = 3
cols = 2
matrix = []
for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(i)

print(matrix)
print()

for i in matrix:
    print(i)