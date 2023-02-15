def create_matrix(size):
    matrix = []
    # Loop through each row and get the input data
    for _ in range(size):
        data = input().split(' ')
        matrix.append(data)

    return matrix

def main_game_logic(matrix):
    # Set initial car coordinates, up and down tunnel coordinates, distance, and finish condition
    car_coordinates = [0, 0]
    up_tunel_coordinate, down_tunel_coordinate = [(i, matrix[i].index('T')) for i in range(len(matrix)) if 'T' in matrix[i]]
    distance = 0
    finish_condition = False

    while True:
        # Get the next command
        command = input()

        # If the command is 'End', update the matrix and return the relevant data
        if command == 'End':
            matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
            return matrix, distance, finish_condition

        # Move the car depending on the command
        elif command == 'down':
            car_coordinates[0] += 1
        elif command == 'up':
            car_coordinates[0] -= 1
        elif command == 'right':
            car_coordinates[1] += 1
        elif command == 'left':
            car_coordinates[1] -= 1

        # If the car enters a tunnel, update the matrix, car coordinates, and distance
        if matrix[car_coordinates[0]][car_coordinates[1]] == 'T':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'
            if tuple(car_coordinates) == up_tunel_coordinate:
                matrix[down_tunel_coordinate[0]][down_tunel_coordinate[1]] = '.'
                car_coordinates = [down_tunel_coordinate[0], down_tunel_coordinate[1]]
            else:
                matrix[up_tunel_coordinate[0]][up_tunel_coordinate[1]] = '.'
                car_coordinates = [up_tunel_coordinate[0], up_tunel_coordinate[1]]

            distance += 30
            continue

        # If the car finishes the race, update the matrix, distance, and finish condition, and return the relevant data
        elif matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            finish_condition = True
            distance += 10
            matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
            return matrix, distance, finish_condition

        # If the car doesn't enter a tunnel or finish the race, update the distance
        distance += 10


def print_function(data, racing_number):
    # Get the matrix, distance, and finish condition from the data
    matrix, distance, finish_condition = data

    # Print whether the car finished the race or not, the distance covered, and the matrix
    if finish_condition:
        print(f'Racing car {racing_number} finished the stage!')
    else:
        print(f'Racing car {racing_number} DNF.')

    print(f'Distance covered {distance} km.')
    for row in matrix:
        print(''.join(row))


# Get the size of the matrix, racing number, and matrix
size = int(input())
racing_number = input()
matrix = create_matrix(size)

# Run the main game logic, get the relevant data, and print the output
print_function(main_game_logic(matrix), racing_number)
