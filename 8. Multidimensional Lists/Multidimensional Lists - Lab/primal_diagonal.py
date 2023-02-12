# The function `read_matrix_func` reads the size of the matrix and inputs the elements of the matrix
# and stores them in a 2-D list `current_matrix`.
def read_matrix_func():
    matrix_size = int(input())
    current_matrix = []
    # Looping through the rows to input the elements
    for row in range(matrix_size):
        # Inputting the elements of the current row as a string and converting them into a list of integers
        row_data = list(map(int,input().split(' ')))
        current_matrix.append(row_data)
    
    return current_matrix

# The function `get_sum_diagonal` takes a matrix as input and returns the sum of the elements in the primary diagonal.
def get_sum__primary_diagonal(matrix):
    sum_primary_diagonal = [matrix[i][i] for i in range(len(matrix))]

    return sum(sum_primary_diagonal)

# The function `get_sum_secondary_diagonal` takes a matrix as input and returns the sum of the elements in the secondary diagonal.
def get_sum_secondary_diagonal(matrix):
    # Calculating the sum of the elements in the secondary diagonal
    sum_secondary_diagonal = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
    # Returning the sum of the secondary diagonal
    return sum(sum_secondary_diagonal)

# The function `get_sum_left_half` takes a matrix as input and returns the sum of the elements in the left half of the matrix.
def get_sum_left_half(matrix):
    # Getting the size of the matrix
    matrix_size = len(matrix)
    # Initializing a variable to store the sum of the left half
    sum_left_half = 0
    # Looping through the rows
    for row in range(matrix_size):
        # Looping through the columns in the current row
        for column in range(row+1):
            # Adding the current element to the sum of the left half
            sum_left_half += matrix[row][column]

    # Returning the sum of the left half
    return sum_left_half

# The function `get_sum_right_half` takes a matrix as input and returns the sum of the elements in the right half of the matrix.
def get_sum_right_half(matrix):
    # Getting the size of the matrix
    matrix_size = len(matrix)
    # Initializing a variable to store the sum of the right half
    sum_right_half = 0
    # Looping through the rows
    for row in range(matrix_size):
        # Looping through the columns in the current row
        for column in range(row, matrix_size):
            # Adding the current element to the sum of the right half
            sum_right_half += matrix[row][column]

    return sum_right_half



matrix = read_matrix_func()

print(get_sum__primary_diagonal(matrix))