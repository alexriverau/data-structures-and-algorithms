from data_structures.hashtable import Hashtable


def left_join(left_hashmap, right_hashmap):
    result = []

    for key in left_hashmap:
        left_value = left_hashmap[key]

        for r_key in right_hashmap:
            if key == r_key:
                right_value = right_hashmap[r_key]
            else:
                right_value = None

    result.append([key, left_value, right_value])

    return result
