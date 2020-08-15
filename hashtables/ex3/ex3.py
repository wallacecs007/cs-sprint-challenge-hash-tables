def intersection(arrays):
    # Creating empty dict and list
    dict = {}
    result = []

    # Looping through arrays provided
    for array in arrays:
        # Looping through numbers in each array
        # While this is a nested loop, usually you would loop through another
        # List while looping through a list. By using a dict, we can check for
        # numbers that have been found already.
        for number in array:
            if number in dict.keys():
                # If it exists, increment it
                dict[number] += 1
            else:
                # Else add it
                dict[number] = 1
    length = len(arrays)
    for key in dict.keys():
        if dict[key] == length:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
