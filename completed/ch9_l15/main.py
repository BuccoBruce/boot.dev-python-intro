def get_champion_slices(champions):
    champions_3_end = champions[2:]
    champions_no_end = champions[:-1]
    champions_even = champions[::2]

    return champions_3_end, champions_no_end, champions_even