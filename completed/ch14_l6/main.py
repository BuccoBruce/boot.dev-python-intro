def divide_list(nums: list[int], divisor: int) -> list[float]:
    new_list = []
    for num in nums:
        new_list.append((num / divisor))
    return new_list
