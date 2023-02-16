def even_odd(*args):
    command = args[-1]
    numbers = []

    for num in args[:-1]:
        if int(num) % 2 == 0 and command == "even":
            numbers.append(num)
        elif int(num) % 2 == 1 and command == "odd":
            numbers.append(num)

    return numbers
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))