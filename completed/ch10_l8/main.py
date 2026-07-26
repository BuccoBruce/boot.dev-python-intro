def get_most_common_enemy(enemies_dict):
    enemy_count = float("-inf")
    enemy = ""
    if not enemies_dict:
        return None
    else:
        for k in enemies_dict:
            if enemies_dict[k] > enemy_count:
                enemy_count = enemies_dict[k]
                enemy = k
    return enemy