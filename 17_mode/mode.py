def mode(nums):
    nums_set = set(nums)
    most_common_num = 0
    num_of_nums = 0
    for num in nums_set:
        count = nums.count(num)
        if count > num_of_nums:
            num_of_nums = count
            most_common_num = num
    return most_common_num

    

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
