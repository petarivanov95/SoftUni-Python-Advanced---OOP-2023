# Define the number of rows and columns for the matrix
rows = 3
cols = 2

# Initialize an empty matrix
matrix = []

# Loop through each row and fill it with integers equal to the row number
for i in range(rows):
    # Initialize a new row in the matrix
    matrix.append([])
    # Loop through each column and fill it with the integer equal to the row number
    for j in range(cols):
        matrix[i].append(i)

# Print the matrix
print(matrix)
print()

# Another way to print the matrix, without using the index
for i in matrix:
    print(i)

# Create another matrix using a nested loop
for row in range(3):
    matrix.append([])
    for col in range(3):
        matrix[row].append(col + (row * 3))

# Create a matrix using list comprehension
matrix_comprehension = [[col + (row * 3) for col in range(3)] for row in range(3)]

# Create a matrix using a lambda function and list comprehension
make_matrix = lambda x, y, fill: [[fill for _ in range(y)] for _ in range(x)] # m[x][y]


# Print the matrix and matrix created using list comprehension
print(matrix)
print(matrix_comprehension)

# Define a sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create a new matrix from the sample matrix, transposing it
new_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

# Print the transposed matrix
print(new_matrix)

# Define a sample 3-dimensional matrix
matrix_3d = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
]

# Access different elements of the 3-dimensional matrix
print(matrix_3d[0]) # First 2D matrix
print(matrix_3d[0][0]) # First row of the first 2D matrix
print(matrix_3d[0][0][0]) # First element of the first row of the first 2D matrix
