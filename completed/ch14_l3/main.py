def remove_nonints(nums: list[object]) -> list[int]:
    list_ints = []

    for num in nums:
        if type(num) is int:
            list_ints.append(num)

    return list_ints
