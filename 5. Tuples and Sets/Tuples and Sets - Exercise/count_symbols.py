# takes in the string
my_input = input()

# takes the unique elements, then into list and then alphabetically sorts
set_vals = sorted(list(set(my_input))) 

# a dictionary for the count values
my_dict = {k: my_input.count(k) for k in set_vals}

for id, val in enumerate(set_vals):
    print(f'{val}: {my_dict[val]} time/s')

