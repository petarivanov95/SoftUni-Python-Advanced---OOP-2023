# def shop_from_grocery_list(budget, grocery_list, *products):

#     prices = {}
#     for grouped in products:
#         item, price = grouped
#         if item in prices.keys():
#             continue
#         else:
#             prices[item] = price

#     purchased = set()
#     total_cost = 0

#     for id in range(len(grocery_list)):
#         if grocery_list[id] not in prices:
#             continue
#         if grocery_list[id]in purchased:
#             continue
#         if budget < prices[grocery_list[id]]:
#             break

#         purchased.add(grocery_list[id])
#         total_cost += prices[grocery_list[id]]
#         budget -= prices[grocery_list[id]]

#     if set(grocery_list) == purchased:
#         return f"Shopping is successful. Remaining budget: {budget:.2f}."
#     else:
#         missing = set(grocery_list) - purchased
#         return f"You did not buy all the products. Missing products: {' '.join(missing)}."

def shop_from_grocery_list(budget, grocery_list, *products):
    purchased = set()
    missing = set(grocery_list)
    budget_left = budget
    
    for product, price in products:
        if product not in missing:
            continue
        if budget_left < price:
            break
        purchased.add(product)
        missing.remove(product)
        budget_left -= price

    if missing:
        missing_str = ", ".join(reversed(list(map(str, missing))))
        return f"You did not buy all the products. Missing products: {missing_str}."
    else:
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."



print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
