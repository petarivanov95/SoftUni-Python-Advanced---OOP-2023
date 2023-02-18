
n, m = map(int, input().split())

playground = []
for i in range(n):
    row = input().split()
    playground.append(row)
    if 'B' in row:
        b_row = i
        b_col = row.index('B')

touched_opponents = 0
moves_made = 0

while True:
    command = input()
    if command == 'Finish':
        break

    new_row = b_row
    new_col = b_col

    if command == 'up':
        new_row -= 1
    elif command == 'down':
        new_row += 1
    elif command == 'left':
        new_col -= 1
    elif command == 'right':
        new_col += 1


    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
        continue

    elif playground[new_row][new_col] == 'O':
        continue

    elif playground[new_row][new_col] == 'P':
        touched_opponents += 1
        moves_made += 1
        playground[new_row][new_col] = '-'
        b_row = new_row
        b_col = new_col

    elif playground[new_row][new_col] == '-':
        moves_made += 1
        playground[b_row][b_col] = '-'
        playground[new_row][new_col] = 'B'
        b_row = new_row
        b_col = new_col

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves_made}')
