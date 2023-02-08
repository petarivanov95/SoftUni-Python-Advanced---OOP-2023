from sys import maxsize

def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key = lambda x: (-len(x[1]),x[0]))
    result = []

    for cheese_name, quantity in sorted_data:
        result.append(cheese_name)
        result.extend(sorted(quantity,reverse = True))

    return '\n'.join([str(x) for x in result])

# def sorting_cheeses(**kwargs):
#     def length_checker(dictionary_data):
#         max_val = -1*maxsize
#         for k,v in dictionary_data.items():
#             if v > max_val:
#                 max_val = v
#         return max_val

#     sorted_data = sorted(kwargs,key = length_checker,reverse=True)
#     return sorted_data

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
