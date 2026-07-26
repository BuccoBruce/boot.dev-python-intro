def calculate_experience_points(level):
    exp = 0
    for i in range(level, 1, -1):
        exp +=  (i - 1) * 5
    return exp