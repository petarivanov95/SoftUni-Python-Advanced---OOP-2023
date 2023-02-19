
num_operations = int(input())
set_cars = set()

for x in range(num_operations):
    direction, car_number = input().split(', ')

    if car_number not in set_cars and direction == 'IN':
        set_cars.add(car_number)
    elif car_number in set_cars and direction == 'OUT':
        set_cars.remove(car_number)

if len(set_cars) == 0:
    print(f'Parking Lot is Empty')
else:
    for x in set_cars:
        print(x)