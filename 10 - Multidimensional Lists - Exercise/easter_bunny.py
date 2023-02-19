# Read the size of the matrix from input
size = int(input())

# Initialize an empty matrix and variables to store bunny position and the best path
matrix = []
bunny_pos = []
best_path = []

# Initialize variables to keep track of the best direction and the maximum number of collected eggs
best_direction = None
max_collected_eggs = 0

# Define a dictionary that maps directions to their respective row and column offsets
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Read the matrix from input and find the position of the bunny
for row in range(size):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

# For each direction, calculate the path and the number of collected eggs
for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]
    path = []
    collected_eggs = 0

    # Continue moving in the current direction until we reach a wall or go out of bounds
    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break

        # Collect eggs and add the current position to the path
        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        # Move to the next position in the current direction
        row += positions[0]
        col += positions[1]

    # If the current direction collects more eggs than the previous best, update the best path and direction
    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

# Output the best direction, the best path, and the maximum number of collected eggs
print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)
