def even_odd_filter(**kwargs):
    # This function takes a dictionary of lists as input and returns a new dictionary
    # containing only the even or odd values, sorted by the length of the lists.

    dict_of_filtered_vals = {}  # Create an empty dictionary to store the filtered values.

    # Loop through the key-value pairs in the input dictionary.
    for k, v in kwargs.items():
        if k == 'odd':
            # If the key is 'odd', add the odd values to the dictionary of filtered values.
            dict_of_filtered_vals[k] = [x for x in v if x % 2 != 0]
        elif k == 'even':
            # If the key is 'even', add the even values to the dictionary of filtered values.
            dict_of_filtered_vals[k] = [x for x in v if x % 2 == 0]

    # Sort the dictionary of filtered values by the length of the lists in descending order.
    sorted_dict = dict(sorted(dict_of_filtered_vals.items(), key=lambda x: -len(x[1])))

    return sorted_dict  # Return the sorted dictionary of filtered values.

# Sample Input
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
