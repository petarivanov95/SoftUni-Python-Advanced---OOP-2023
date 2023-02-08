shopping_list = {}

def show_list(shopping_list):

    for item_name, quantity in shopping_list.items():
        print(f'{quantity} x {item_name}')

def add_items(shopping_list, **things_to_buy):
    for item_name, quantity in things_to_buy.items():
        shopping_list[item_name] = quantity

    return shopping_list

shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
show_list(shopping_list)