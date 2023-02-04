from collections import deque

food_qty = int(input())

orders = deque([int(n) for n in input().split()])

print(max(orders))

local_orders = orders.copy() # create a copy for the loop, which will not be affected by the queue changes

for order in local_orders:
    if food_qty - order >= 0: # checks for food availability
        orders.popleft() # removes FIFO order
        food_qty -= order # subtracts the particular order from the total food qty we have
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders])}")
        break
else:
    print("Orders complete")