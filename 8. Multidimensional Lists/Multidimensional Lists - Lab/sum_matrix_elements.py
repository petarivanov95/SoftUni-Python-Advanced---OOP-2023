rows, cols = map(int, input().split(', '))
matrix = []

for r in range(rows):
    row_data = list(map(int,input().split(', ')))
    matrix.append(row_data)

print(matrix, end='')