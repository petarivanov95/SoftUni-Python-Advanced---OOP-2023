# solution 1

def stock_availability(inventory, action, *args):

    if action == 'delivery':
            inventory.extend(args)
    elif action == 'sell':
        if len(args) == 0:
            inventory.pop(0)

        elif isinstance(args[0],int):
            boxes = args[0]
            for x in range(boxes):
                inventory.pop(0)

        elif not isinstance(args[0],int):
            for order in args:
                while order in inventory:
                    inventory.remove(order)

    return inventory

# solution 2
def stock_availability(inventory, action, *args):
    if action == "delivery":
        inventory += list(args)
    elif action == "sell":

        if not args:
            inventory.pop(0)

        elif isinstance(args[0], int):
            sold = args[0]
            inventory = inventory[sold:]

        else:
            flavors = set(args)
            inventory = [item for item in inventory if item not in flavors]
    return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
