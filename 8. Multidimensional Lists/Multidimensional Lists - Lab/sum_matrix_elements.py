rows, cols = map(int, input().split(', '))
matrix = []

for r in range(rows):
    row_data = list(map(int,input().split(', ')))
    matrix.append(row_data)
    # for c in cols:
    #     info = list(map(int, input.split(', ')))
    #     matrix[c].extend(info)

print(matrix, end='')
