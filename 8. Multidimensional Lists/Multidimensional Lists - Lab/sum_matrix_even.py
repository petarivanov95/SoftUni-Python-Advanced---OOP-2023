number_of_rows = int(input())

matrix = []

for x in range(number_of_rows):
    column = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(column)


print(matrix)