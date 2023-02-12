def flights(*args):
    flight_dict = {}
    flight_all = args
    for i, arg in enumerate(flight_all):
        if arg == "Finish":
            break
        elif isinstance(arg, int):
            if flight_dict[flight_all[i-1]] in flight_dict:
                flight_dict[flight_all[i-1]] += arg
            else:
                flight_dict[flight_all[i-1]] = arg
        else:
            pass
    return flight_dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))