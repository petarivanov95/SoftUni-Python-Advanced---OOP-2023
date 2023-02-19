size = int(input())

cruisers = 3
bombs_hit = 0

matrix = []
submarine_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Read in the matrix
for row in range(size):
    line = list(input())
    matrix.append(line)

    # Record the position of the submarine and remove it from the matrix
    if "S" in line:
        submarine_pos = [row, line.index("S")]
        matrix[row][submarine_pos[1]] = "-"

# Simulate the submarine's movement and attacks
while cruisers:
    direction = input()

    # Calculate the new position of the submarine based on the chosen direction
    current_row = directions[direction][0] + submarine_pos[0] # Starting from S pos + dict val
    current_col = directions[direction][1] + submarine_pos[1] # Starting from S pos + dict val

    # Update the position of the submarine
    submarine_pos = [current_row, current_col]

    # Check if a cruiser or bomb was hit and update the matrix
    if matrix[current_row][current_col] == "C":
        cruisers -= 1
    elif matrix[current_row][current_col] == "*":
        bombs_hit += 1

        # If the submarine is hit by 3 bombs, print a failure message and exit the loop
        if bombs_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
            break

    matrix[current_row][current_col] = "-"

# If all cruisers were destroyed, print a success message and update the matrix with the submarine's position
else:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    matrix[submarine_pos[0]][submarine_pos[1]] = "S"

# Print the updated matrix
[print(*row, sep='') for row in matrix]
