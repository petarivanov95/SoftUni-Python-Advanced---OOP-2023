line = input().split("|")  

# Initializing an empty list to store the final list of sub-strings
sub_lists = []  

# Looping through the sub-strings in reverse order
for sub_string in line[::-1]: 
    # Splitting each sub-string into individual words and adding them to the final list
    sub_lists.extend(sub_string.split())

# Joining the final list of sub-strings into a single string with a space between each word
result = ' '.join(sub_lists)
print(result)
