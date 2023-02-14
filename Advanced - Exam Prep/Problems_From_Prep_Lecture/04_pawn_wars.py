# Define a function to get the current player's position in the matrix
def get_player_position(matrix, player):
    # Iterate over each row in the matrix and check if the player is in the row
    for row_index, row_data in enumerate(matrix):
        if player in row_data:
            # If the player is found, return their position as a tuple of (row, column)
            return row_index, row_data.index(player)

# Define the main game logic
def main_game_logic():
    # Set the number of rows and columns to 8, and set the initial players
    rows, columns = 8, 8
    current_player, second_player = 'w', 'b'
    # Read in the matrix from user input as a list of lists
    matrix = [input().split(' ') for _ in range(rows)]
    # Get the positions of the current and second players using the get_player_position function
    current_player_position = get_player_position(matrix, current_player)
    second_player_position = get_player_position(matrix, second_player)
    # Set the initial movement direction for each player
    current_change, second_change = -1, +1
    # Set initial conditions for winning the game
    capture_condition, queen_condition = False, False

    # Loop until the game is over (either a capture or promotion to queen occurs)
    while not queen_condition and not capture_condition:
        # Get the current player's row and column
        current_player_row, current_player_column = current_player_position
        # Move the current player one row forward in the direction set by current_change
        current_player_row += current_change
        current_player_position = (current_player_row, current_player_column)

        # Check if the current player can capture the second player
        if current_player_row == second_player_row and abs(current_player_column - second_player_column) == 1:
            capture_condition = True
            current_player_position = (current_player_row, second_player_column)
        # Check if the current player has reached the other end of the board and can promote to a queen
        elif current_player_row in [0, rows - 1]:
            queen_condition = True
        # If neither condition is met, swap the positions and change directions for the players
        else:
            current_player_position, second_player_position = second_player_position, current_player_position
            current_change, second_change = second_change, current_change
            current_player, second_player = second_player, current_player

    # Return the winning position, the winning player, and whether a capture occurred
    return current_player_position, current_player, capture_condition

# Define a function to print the end of game message based on the winning position, player, and capture condition
def print_function(position_data, player_win, capture_condition):
    # Get the row and column of the winning position
    row, column = position_data
    # Define the row and column names for the board
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # Get the name of the winning position as a string (e.g. "d5")
    position_name = f'{column_names[column]}{row_names[row]}'

    # If a capture occurred, print a message saying which player won and where the capture occurred
    if capture_condition:
        return f'Game over! {player_win} win,
