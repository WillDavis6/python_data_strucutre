def remove_every_other(lst):
    new_lst = []
    [new_lst.append(item) for item in lst if lst.index(item) % 2 != 1]
    return new_lst

    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
