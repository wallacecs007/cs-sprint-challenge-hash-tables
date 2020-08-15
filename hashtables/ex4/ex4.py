def has_negatives(a):
    # Creating empty dict and list
    dict = {}
    result = []
    # Looping through each value in the array
    for number in a:
        # Checkint to see if the dict has the number on the opposite side of zero
        # If 1 checking for -1, if -1 checking for 1.
        if (number * -1) in dict.keys():
            # If found, see if number is positive. If so append it.
            if number > 0:
                result.append(number)
            # If not, append the value at the dict location.
            else:
                result.append(dict[number * -1])
        # If it doesn't exist, add it to the dict.
        else:
            dict[number] = number

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
