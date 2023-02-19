from collections import deque


names_deque = deque() # create a double-ended queue to store the names

# define the command strings for ending the loop and removing names from the queue
command_end = 'End'
command_paid = 'Paid'


while True:

    command = input()     # get the command from the user

    # if the command is 'End', print the number of names remaining and break the loop
    if command == command_end:
        print(f'{len(names_deque)} people remaining.')
        break

    # if the command is 'Paid', remove and print each name from the left side of the queue
    elif command == command_paid:
        while names_deque:
            print(names_deque.popleft())
    
    # if the command is not 'End' or 'Paid', add it as name to the right side of the queue
    else:
        names_deque.append(command)
