def merge(dict1, dict2):
    merged_dict = {}

    for k in dict1:
        merged_dict[k] = dict1[k]

    for k in dict2:
        merged_dict[k] = dict2[k]

    return merged_dict
