size = int(input())
matrix = [[int(n) for n in input().split()] for _ in range(size)]


command = input().split()

while command[0] != 'END': 
    type_command, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])


    if row < 0 or row >= size or col < 0 or col >= size:
        print('Invalid coordinates')
    elif type_command == 'Add':
        matrix[row][col] += num
    elif type_command == 'Subtract':
        matrix[row][col] -= num

    command = input().split()

for row in matrix:
    print(*row)





# def read_matrix():
#     # Get the size of the matrix from user input
#     matrix_size = int(input())
#     # Create an empty matrix to hold the data
#     a_matrix = []

#     for row in range(matrix_size):
#         row_info = list(map(int,input().split()))
#         # Add the row data to the matrix
#         a_matrix.append(row_info)

#     return a_matrix

# # Call the read_matrix function to get user input and store the resulting matrix in my_matrix variable
# my_matrix = read_matrix()

# def modify_matrix(matrix):

#     command = ' '
#     # Start an infinite loop until the 'END' command is received
#     while True:
#         # Read user input and split it into separate values
#         info = input().split()
#         # Check if the command is 'END'
#         if len(info) > 1:
#             command = info[0]
#             row = int(info[1])
#             col = int(info[2])
#             new_val = int(info[3])
#         else:
#             command = info[0]
        
#         # If the 'END' command is received, break out of the loop
#         if command == 'END':
#             break
        
#         # Check if the coordinates are within the matrix range
#         if not 0 > row > len(matrix) or not 0 > col > len(matrix):
#             return "Invalid coordinates" 

#         # If the command is 'Add', modify the matrix by adding a value to the specified cell
#         if command == 'Add':
#             matrix[row][col] += new_val
#         # If the command is 'Subtract', modify the matrix by subtracting a value from the specified cell
#         elif command == 'Subtract':
#             matrix[row][col] -= new_val

#     # Return the modified matrix to the caller
#     return matrix

# # Call the modify_matrix function to get user input and modify the my_matrix variable accordingly
# result = modify_matrix(my_matrix)

# # Loop over the resulting matrix and print its values
# if result == 'Invalid coordinates':
#     print(result)
# else:
#     for row in result:
#         print(*row)