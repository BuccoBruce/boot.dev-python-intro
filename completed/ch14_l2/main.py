def find_min(nums: list[int]) -> int | float:
    minimum: float = float("inf")

    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
