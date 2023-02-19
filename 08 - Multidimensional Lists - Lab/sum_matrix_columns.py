def read_matrix_func():
    number_of_rows, number_of_cols = map(int, input().split(', '))

    current_matrix = []
    for row in range(number_of_rows):
        row_data = list(map(int,input().split(' ')))
        current_matrix.append(row_data)

    return current_matrix


def get_sum_columns():
    matrix = read_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    sum_of_columns = []

    for x in range(columns):
        tmp_sum = 0
        for y in range(rows):
            tmp_sum += matrix[y][x]
        sum_of_columns.append(tmp_sum)
        
    return sum_of_columns

one_matrix_sum = get_sum_columns()

print('\n'.join(map(str, one_matrix_sum)))