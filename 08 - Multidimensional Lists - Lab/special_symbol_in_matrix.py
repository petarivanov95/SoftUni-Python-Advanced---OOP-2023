def read_matrix_func():
    # Prompt the user for the number of rows in the matrix
    number_of_rows = int(input())
    current_matrix = []

    # Loop through the number of rows and create a two-dimensional matrix based on the user's inputs
    for row in range(number_of_rows):
        row_data = list(input())
        current_matrix.append(row_data)

    return current_matrix

def check_func_for_special_symbol(matrix, symbol):
    # Loop through the rows and columns of the matrix and check if the special symbol is present
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            current_element = matrix[row][col]
            if current_element == symbol:
                return row, col

def print_func(data, symbol):
    # Check if the special symbol is present in the matrix
    if data:
        print(data)
    else:
        # If the symbol does not occur in the matrix, print a message indicating this
        print(f'{symbol} does not occur in the matrix')

# Call the read_matrix_func function to create the matrix
matrix = read_matrix_func()

# Prompt the user for the special symbol
special_symbol = input()

# Call the check_func_for_special_symbol and print_func functions with the matrix and special symbol as arguments
print_func(check_func_for_special_symbol(matrix, special_symbol), special_symbol)
