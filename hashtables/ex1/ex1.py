def get_indices_of_item_weights(weights, length, limit):
    # Setting up an empty Dict
    dict = {}
    # Defining an indice counter
    indice = 0
    # Looping over each weight
    for item in weights:
        # Check if the weight is in the hashtable that matches the current check
        # If so return the indices, largest (newest item) first.
        if limit - item in dict.keys():
            return [indice, dict[limit - item]]
        # Else add item to hashtable
        else:
            dict[item] = indice
        indice += 1

    # Nothing found, return none.
    return None
