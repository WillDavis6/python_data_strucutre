#def fn(entry):
 #   if entry % 2 == 0:
  #      return True
 #   else:
 #       return False

def partition(lst, fn):
    lst1 = []
    lst2 = []
    for item in lst:
        if fn(item) == True:
            lst1.append(item)
        elif fn(item) == False:
            lst2.append(item)
    return lst1, lst2

    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """