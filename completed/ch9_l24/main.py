def check_ingredient_match(recipe, inventory):
    obtained_count = 0
    missing_count = 0
    items_missing = []
    percentage_completed = 0.0

    for ingredient in recipe:
        if ingredient in inventory:
            obtained_count += 1
        else:
            missing_count += 1
            items_missing.append(ingredient)

    percentage_completed = (obtained_count / len(recipe)) * 100

    return percentage_completed, items_missing
