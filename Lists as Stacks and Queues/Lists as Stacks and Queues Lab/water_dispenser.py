from collections import deque

water_amount = int(input())

command_start = 'Start'
command_end = 'End'
command_refill = 'refill'

def add_names_in_deque():
    people_data = deque()
    while True:
        name = input()

        if name == command_start:
            break
        people_data.append(name)
    return people_data

people_deque = add_names_in_deque()

while True:
    command = input()

    if command == command_end:
        print(f"{water_amount} liters left")
        break

    elif command.startswith(command_refill):
        refill_command_data = command.split(' ')
        refill_water_amount = int(refill_command_data[1])
        water_amount += refill_water_amount

    else:
        person = people_deque.popleft()
        current_litres = int(command)
        if current_litres <= water_amount:
            print(f'{person} got water')
            water_amount -= current_litres
        else:
            print(f'{person} must wait')
