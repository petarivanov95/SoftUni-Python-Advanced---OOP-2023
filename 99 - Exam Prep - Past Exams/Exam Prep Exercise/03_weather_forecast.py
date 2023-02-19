def forecast2(*data):
    result = []

    def add_locations(type_of_location):  # define a function to add locations of a certain type to the results
        locations = list(filter(lambda x: x[1] == type_of_location, data))  # use filter to get locations that match the specified weather type
        [result.append(f"{l[0]} - {type_of_location}") for l in sorted(locations)]  # add the locations to the result list, sorted in alphabetical order

    add_locations("Sunny")  # call the function to add sunny locations
    add_locations("Cloudy")  # call the function to add cloudy locations
    add_locations("Rainy")  # call the function to add rainy locations

    return '\n'.join(result)  # return the result list as a string with newlines between each location


def forecast(*data):
    result = []

    def add_locations(type_of_location):  # define a function to add locations of a certain type to the results
        locations = []  # create an empty list to store the matching locations

        for location, weather in data:  # iterate over each location and weather pair
            if weather == type_of_location:  # if the weather matches the specified type
                locations.append(location)  # add the location to the list

        for l in sorted(locations):  # iterate over the sorted list of matching locations
            result.append(f"{l} - {type_of_location}")  # add the location to the result list with the weather type

    add_locations("Sunny")  # call the function to add sunny locations
    add_locations("Cloudy")  # call the function to add cloudy locations
    add_locations("Rainy")  # call the function to add rainy locations

    return '\n'.join(result)  # return the result list as a string with newlines between each location


print(forecast2(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))  # print the result of the forecast2 function with the specified location and weather data
