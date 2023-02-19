# Read the size of the board
size = int(input())

# Read the board matrix
matrix = [list(input()) for _ in range(size)]

# Define all possible moves for a knight
moves = (
    (-2, -1),  # Up 2 and left 1
    (-2, 1),   # Up 2 and right 1
    (-1, -2),  # Up 1 and left 2
    (-1, 2),   # Up 1 and right 2
    (2, 1),    # Down 2 and right 1
    (2, -1),   # Down 2 and left 1
    (1, 2),    # Down 1 and right 2
    (1, -2)    # Down 1 and left 2
)

# Initialize the counter for the removed knights
removed_knights = 0

# Repeat the process until there are no more knights to remove
while True:
    # Initialize the counter for the maximum number of attacks
    max_attacks = 0

    # Initialize the position of the knight with the most attacks
    knight_with_most_attacks_pos = []

    # Iterate over each cell in the board
    for row in range(size):
        for col in range(size):
            # Check if there is a knight in the current cell
            if matrix[row][col] == "K":
                # Initialize the counter for the number of attacks of the current knight
                attacks = 0

                # Check all possible moves for the current knight
                for move in moves:
                    # Calculate the new position after the move
                    new_row = row + move[0]
                    new_col = col + move[1]

                    # Check if the new position is inside the board
                    if 0 <= new_row < size and 0 <= new_col < size:
                        # Check if there is a knight in the new position
                        if matrix[new_row][new_col] == "K":
                            # Increment the counter of the number of attacks
                            attacks += 1

                # Check if the current knight has more attacks than the previous knights
                if attacks > max_attacks:
                    # Update the position of the knight with the most attacks
                    knight_with_most_attacks_pos = [row, col]
                    # Update the maximum number of attacks
                    max_attacks = attacks

    # Check if there is a knight to remove
    if knight_with_most_attacks_pos:
        # Remove the knight from the board
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        # Increment the counter of removed knights
        removed_knights += 1
    else:
        # If there are no more knights to remove, exit the loop
        break

# Print the total number of removed knights
print(removed_knights)
