
def read_matrix_func():
    matrix_size = int(input())
    current_matrix = []
    # Looping through the rows to input the elements
    for row in range(matrix_size):
        # Inputting the elements of the current row as a string and converting them into a list of integers
        row_data = list(map(int,input().split(', ')))
        current_matrix.append(row_data)
    
    return current_matrix

def get_primary_diagonal(matrix):

    primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    return primary_diagonal

def get_secondary_diagonal(matrix):
    # Calculating the sum of the elements in the secondary diagonal
    secondary_diagonal = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
    # Returning the sum of the secondary diagonal
    return secondary_diagonal


matrix = read_matrix_func()

primary = get_primary_diagonal(matrix)
secondary = get_secondary_diagonal(matrix)
sum_primary = sum(primary)
sum_secondary = sum(secondary)


print(f'Primary diagonal: {", ".join(list(map(str,primary)))}. Sum: {sum_primary}')
print(f'Secondary diagonal: {", ".join(list(map(str,secondary)))}. Sum: {sum_secondary}')