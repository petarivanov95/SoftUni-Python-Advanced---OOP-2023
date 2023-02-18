def main_game_logic():
    # This function gets the position of a player on the matrix
    def get_player_position(matrix, player):
        for row_index, row_data in enumerate(matrix):
            if player in row_data:
                return row_index, row_data.index(player)

    rows, columns = 8, 8
    current_player, second_player = 'w', 'b'
    # Input matrix from the user as a 2D list
    matrix = [input().split(' ') for _ in range(rows)]
    # Get the starting positions of each player
    current_player_position = get_player_position(matrix, current_player)
    second_player_position = get_player_position(matrix, second_player)
    current_change, second_change = -1, +1
    capture_condition, queen_condition = False, False

    # Loop until the queen or capture condition is met
    while not queen_condition and not capture_condition:
        current_player_row, current_player_column = current_player_position
        second_player_row, second_player_column = second_player_position

        # Move the current player's pawn one row forward
        current_player_row += current_change
        current_player_position = (current_player_row, current_player_column)

        # Check if the current player can capture the second player's pawn
        if abs(current_player_column - second_player_column) == 1:
            if current_player == 'w' and current_player_row + current_change == second_player_row:
                capture_condition = True
                current_player_position = (current_player_row + current_change, second_player_column)
            elif current_player == 'b' and current_player_row + second_change == current_player_row:
                capture_condition = True
                current_player_position = (current_player_row + current_change, second_player_column)
        # Check if the current player's pawn has reached the other end and needs to be promoted to a queen
        elif current_player_row in [0, rows - 1]:
            queen_condition = True
        else:
            # Swap the positions of the two players and change the direction of their movement
            current_player_position, second_player_position = second_player_position, current_player_position
            current_change, second_change = second_change, current_change
            current_player, second_player = second_player, current_player

    # Return the final position of the current player's pawn, which will be used for printing the result
    return current_player_position, current_player, capture_condition


def print_function(position_data, player_win, capture_condition):
    # Extract the row and column from the position data and use them to create a position name in chess notation
    row, column = position_data
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    position_name = f'{column_names[column]}{row_names[row]}'

    # Print the appropriate message based on whether the game ended due to a capture or promotion to queen
    if capture_condition:
        return f'Game over! {player_win} win, capture on {position_name}.'
    else:
        return f'Game over! {player_win} pawn is promoted to a queen at {position_name}.'
