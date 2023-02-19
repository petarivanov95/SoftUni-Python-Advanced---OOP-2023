from collections import deque

# Get input for the number of ramen bowls and customers
ramen_bowls = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

# Simulate the ramen restaurant
while customers:
    # If there are no more ramen bowls, print a message and exit the loop
    if not ramen_bowls:
        print(f"Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break

    # Serve the next customer and deduct a ramen bowl
    customer = customers.popleft()
    bowl = ramen_bowls.pop()

    # If the customer's order cannot be fulfilled, add the remaining order back to the queue
    if customer > bowl:
        customers.appendleft(customer - bowl)
    # If there are leftover ramen bowls, add them back to the deque
    elif customer < bowl:
        ramen_bowls.append(bowl - customer)
        
# If all customers are served, print a success message and the number of leftover ramen bowls
else:
    print(f"Great job! You served all the customers.")

    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen_bowls))}")
