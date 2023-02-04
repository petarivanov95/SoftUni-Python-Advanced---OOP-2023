from collections import deque

names_deque = deque()
command_end = 'End'
command_paid = 'Paid'

while True:
    command = input()

    if command == command_end:
        print(f'{len(names_deque)} people remaining.')
        break

    elif command == command_paid:
        while names_deque:
            print(names_deque.popleft())
    
    else:
        names_deque.append(command)

