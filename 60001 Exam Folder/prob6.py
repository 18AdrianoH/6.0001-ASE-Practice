def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
    If they are permutations of each other, returns a tuple of 2 items in this order: 
      1) number of times the most frequently occurring element appears
      2) the type of the most frequently occurring element (if there is a tie for most occurring, pick one)
    If both lists are empty, returns the tuple (None, None).
    '''
    if len(L1) == 0 and len(L2) == 0:
        return (None,None)
    else:
        # we will use hashmaps because they are o(1) when we search meaning instead of o(n^2 or cubed we'll be getting o(kn) ~ o(n) where k is a const)
        d1 = {}
        d2 = {}
        # values are gonna be counters
        for item1 in L1:
            if d1.__contains__(item1):
                d1[item1] = d1[item1] + 1
            else:
                d1[item1] = 1
        for item2 in L2:
            if d2.__contains__(item2):
                d2[item2] = d2[item2] + 1
            else:
                d2[item2] = 1
        
        # now check for equality (really disequality because that's how we break)
        for key in d1:
            if not d2.__contains__(key):
                return False
            elif not d2[key] == d1[key]:
                return False

        # now we find the most common number
        mode = L1[0]
        for key in d1: # note that now we know that d1 and d2 are the "same"
            if d1[key] > d1[mode]:
                mode = key
            pass
        # and return the tuple of this mode
        return (d1[mode], type(mode))

print is_list_permutation([1, 'b', 1, 'c', 'c', 1],['c', 1, 'b', 1, 1, 'c'])
print is_list_permutation(['a', 'a', 'b'],['a', 'b'])