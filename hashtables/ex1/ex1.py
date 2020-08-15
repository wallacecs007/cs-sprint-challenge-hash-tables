def get_indices_of_item_weights(weights, length, limit):
    # Setting up an empty Dict
    dict = {}

    for item in weights:
        if item in dict.keys():
            print(dict[item])
            print(item)
            return [dict[item], item]
        else:
            dict[limit - item] = item

    return None


weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)
weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)
