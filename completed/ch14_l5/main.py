def area_sum(rectangles: list[dict[str, int]]) -> int:
    total = 0
    for rectangle in rectangles:
        total += (rectangle["height"] * rectangle["width"])
    return total

