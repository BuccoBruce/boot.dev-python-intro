def reverse_list(items):
    reverse_items = []

    for i in range(len(items) - 1, -1, -1):
        reverse_items.append(items[i])

    return reverse_items
