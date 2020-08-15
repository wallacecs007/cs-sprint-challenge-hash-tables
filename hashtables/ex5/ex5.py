def finder(files, queries):
    # Creating an empty list and dict
    dict = {}
    result = []

    for file in files:
        # Breaking the file out by the / divider for paths
        split = file.split("/")
        # Getting the last part of the file path which is the file name
        # we are searching for
        name = split[-1]

        # Creating an array to store multiple file paths
        if name not in dict.keys():
            dict[name] = []

        # Adding the filepath
        dict[name].append(file)

    # Going through every query, and seeing if it has files associated with it.
    for query in queries:
        if query in dict.keys():
            result.extend(dict[query])

    print(result)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
