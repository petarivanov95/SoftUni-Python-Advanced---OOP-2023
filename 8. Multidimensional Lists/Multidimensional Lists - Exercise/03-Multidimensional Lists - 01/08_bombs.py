n = int(input())

def read_matrix_func(size):
    matrix_size = size
    current_matrix = []
    # Looping through the rows to input the elements
    for row in range(matrix_size):
        # Inputting the elements of the current row as a string and converting them into a list of integers
        row_data = list(map(int,input().split()))
        current_matrix.append(row_data)
    
    return current_matrix

matrix = read_matrix_func(n)
coordinates = ((int(x) for x in x.split(",")) for x in input().split())

directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, 1),    # right
    (0, -1),   # left
    (-1, 1),   # top-right
    (-1, -1),  # top-left
    (1, -1),   # bottom-left
    (1, 1),    # bottom-right
    (0, 0),    # current (this should be last)
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*[matrix[r][c]for c in range(n)], sep=" ") for r in range(n)]