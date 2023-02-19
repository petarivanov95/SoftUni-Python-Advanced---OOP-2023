def math_operations(*numbers, **kwargs):
    # Loop through the input numbers
    for i,x in enumerate(numbers):
        # Determine which keyword argument to use for this iteration
        key = list(kwargs.keys())[i % 4]

        # Update the keyword argument based on the selected operation
        if key == "a":  # Addition
            kwargs[key] += numbers[i]
        elif key == "s":  # Subtraction
            kwargs[key] -= numbers[i]
        elif key == "d":  # Division
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == "m":  # Multiplication
            kwargs[key] *= numbers[i]

    # Sort the keyword arguments based on their values, in descending order
    # (if values are equal, sort by key in ascending order)
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    # Convert the sorted keyword arguments to a string with the desired format
    return '\n'.join(f"{k}: {v:.1f}" for k, v in kwargs)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))