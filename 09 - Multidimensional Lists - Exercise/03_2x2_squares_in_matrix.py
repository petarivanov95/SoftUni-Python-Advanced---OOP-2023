def read_matrix_func():
    rows, cols = [int(x) for x in input().split()]
    current_matrix = []
    # Looping through the rows to input the elements
    for row in range(rows):
        # Inputting the elements of the current row as a string and converting them into a list of integers
        row_data = list(input().split())
        current_matrix.append(row_data)
    
    return current_matrix

equal_blocks = 0
matrix = read_matrix_func()

rows = len(matrix)
cols = len(matrix[0])

for row in range(rows - 1):
    for col in range(cols-1):
        symbol = matrix[row][col]

        if matrix[row][col+1] == symbol and matrix[row+1][col] == symbol and matrix[row+1][col+1] == symbol:
            equal_blocks += 1

print(equal_blocks)