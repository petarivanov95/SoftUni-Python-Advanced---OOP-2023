def multiply(*args):
    result = 1
    for x in range(len(args)):
        result *= args[x]

    return result



print(multiply(1,2,3))