def f_on_some(f, L):
    ls = []
    """
    f: function that maps one int to a boolean
    L: a list
    Returns a sorted list (ascending order) of all unique ints 
    in L that return True when f is applied to them. 
    """
    for num in L:
        if f(num) == True and ls.__contains__(num) == False:
            ls.append(num)
        pass
    ls.sort()
    return ls

## TESTING
#def f(a):
#    return a == 2 or a == 3
#L = [2, 1, 2, 3]
#print(f_on_some(f, L))

def is_power_of_2(x):
    """
    x: an int
    Returns True if there exists a positive int, p, such that 2**p == x
    This function must be recursive.
    """
    # just in case, though it would be better to through an exception for type errors
    if type(x) != int or x % 2 != 0 or x <= 0:
        return False
    elif (x == 2) or (x == 1):
        return True
    else:
        return is_power_of_2(x/2)


print is_power_of_2(3)
print is_power_of_2(-2)
print is_power_of_2(16)
print is_power_of_2(32)
print is_power_of_2(64)
print is_power_of_2(2**50)
print is_power_of_2(0.1)
print is_power_of_2('spaghet')