
def read_matrix_func():
    # Get the number of rows and columns of the matrix from the user input
    number_of_rows, number_of_cols = map(int, input().split(', '))

    current_matrix = []

    # Loop through each row of the matrix
    for row in range(number_of_rows):
        # Get the elements of the current row from the user input
        row_data = list(map(int,input().split(', ')))
        
        # Add the current row to the matrix
        current_matrix.append(row_data)

    # Return the matrix after it has been read and populated with data
    return current_matrix


matrix = read_matrix_func()

# Initialize a variable to store the sum of all elements of the matrix
matrix_elem_sum = 0 


## 1st method - loops through each element of the matrix twice
# for i in matrix:
#     for j in i:
#         matrix_elem_sum += j


## 2nd method - loops through each row of the matrix and sums up the elements of each row using the built-in sum function
# for i in range(len(matrix)):
#     current_row = matrix[i]
#     row_sum = sum(current_row)
#     matrix_elem_sum += row_sum


# 3rd method - enumerate function to loop through the matrix and sums up the elements of each row using the built-in sum function
for id, row in enumerate(matrix):
    matrix_elem_sum += sum(matrix[id])


# 4th method -  a list comprehension to loop through the matrix and sums up the elements of each row
# The result is a single number, the sum of all elements of the matrix
# matrix_elem_sum = sum([sum(matrix[id]) for id,row in enumerate(matrix)])

print(matrix_elem_sum)
print(matrix)