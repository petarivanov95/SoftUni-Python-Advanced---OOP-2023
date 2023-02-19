
def numbers_searching(*args):
    # Find the minimum and maximum values in the input
    min_val = min(args)
    max_val = max(args)
    
    # Create a set of all the numbers in the input
    num_set = set(args)
    
    # Create a set of all the numbers between min_val and max_val (inclusive)
    full_range = set(range(min_val, max_val+1))
    
    # The missing number is the difference between the full range and the input set
    missing_num = list(full_range - num_set)
    
    # The duplicate numbers are found by counting the number of occurrences of each number in the input
    duplicate_nums = [num for num in args if args.count(num) > 1]
    
    # Remove duplicate elements from the duplicate_nums list
    duplicate_nums = list(set(duplicate_nums))
    
    # Return the results in the desired format
    return [missing_num[0], sorted(duplicate_nums)]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
