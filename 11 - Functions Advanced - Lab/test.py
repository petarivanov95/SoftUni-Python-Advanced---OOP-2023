# shopping_list = {}

# def show_list(shopping_list):

#     for item_name, quantity in shopping_list.items():
#         print(f'{quantity} x {item_name}')

# def add_items(shopping_list, **things_to_buy):
#     for item_name, quantity in things_to_buy.items():
#         shopping_list[item_name] = quantity

#     return shopping_list

# shopping_list = add_items(shopping_list, coffee=1, tea=2, cake=1, bread=3)
# show_list(shopping_list)


# languages = ['python', 'c', 'ruby', 'java']
# print(sorted(languages, key = select_first_character))
# def select_first_character(word):
#     return word[0]
# print(sorted(languages, key = select_first_character))


# numbers = [-2, 3, -1, 5]

# print(numbers) # prints the list 
# print(sorted(numbers)) #prints the sorted list (ascending)
# print(sorted(numbers, key=abs)) # sorts based on abs value of items

# numbers = [3, 1, 2, 4, 8, 9, 11]

# print(numbers) # prints the list 
# print(sorted(numbers, key = lambda x: x % 2 == 0 )) # prints the list

names = ['Ivan', 'George', 'Emi','Henrietta']

print(names)
print(sorted(names))
print(sorted(names, key = len))