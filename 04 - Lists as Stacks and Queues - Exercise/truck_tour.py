from collections import deque

num_pumps = int(input())

my_queue = deque()

for x in range(num_pumps):
    pump_station, distance = input().split()
    my_queue.append([int(pump_station),int(distance)])

copied_queue = my_queue.copy()
index = 0
tank = 0

while copied_queue:
    petrol, distance = copied_queue.popleft()
    tank += petrol
    if tank - distance < 0:
        my_queue.rotate(-1)
        copied_queue = copied_queue.copy()
        index += 1
        tank = 0
    else:
        tank -= distance

print(index)