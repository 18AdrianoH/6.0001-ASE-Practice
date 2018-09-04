print 'running code'

def occurs_max_times(L):
    """
    L: a list of ints
    Returns the element in L that occurs the most often in L.
    In case of a tie, returns the maximum of the tied values.
    Raises a ValueError if L is empty.
    """
    if L == None or len(L) == 0:
        raise ValueError("Empty or Null List")

    dic = {}
    for item in L:
        if dic.__contains__(item):
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
        pass

    mode = L[0]
    for key in dic:
        if dic[key] > dic[mode]:
            mode = key
        elif dic[key] == dic[mode]:
            mode = max(key,mode)
        else:
            pass
    return mode


#
# FIX ME PLEASE
#
'''
def count_digits_in_dict(d, digit):
    """
    d: a dict that maps int:int
    digit: an int 0 <= digit <= 9
    Returns a how many times the digit
    occurs in all the values of d. (not the keys)
    """

    if digit < 0 or digit > 9 or type(digit) != int or type(d) != dict:
        raise ValueError("wrong type")

    elif len(d) < 1:
        return 0

    values = []
    times = 0
    for key in d:
        values.append(d[key])
    
    #print values

    for number in values:
        while number > 0:
            if number % 10 == digit or number == digit:
                print number
                times = times + 1
            number = number / 10
            pass
        pass
    return times
'''

### ANOTHER SWINDELED SOLUTION
'''
def count_digits_in_dict(d, digit):
    """
    d: a dict that maps int:int
    digit: an int 0 <= digit <= 9
    Returns a how many times the digit
    occurs in all the values of d. (not the keys)
    """
    if digit < 0 or digit > 9 or type(digit) != int or type(d) != dict:
        raise ValueError("wrong type")

    elif len(d) < 1:
        return 0

    else:
        values = []
        for key in d:
            values.append(d[key])
        digits = []
        for value in values:
            while value > 0:
                digits.append(value%10)
                value = value / 10
        times = 0
        print(digits) # this is for bugtesting
        for dig in digits:
            if dig == digit:
                times = times + 1
        return times
'''

### STRING SOLUTION ATTEMPT
def count_digits_in_dict(d, digit):
    """
    d: a dict that maps int:int
    digit: an int 0 <= digit <= 9
    Returns a how many times the digit
    occurs in all the values of d. (not the keys)
    """
    if digit < 0 or digit > 9 or type(digit) != int or type(d) != dict:
        raise ValueError("wrong type")

    elif len(d) < 1:
        return 0
    #else
    values = []
    for key in d:
        print values
        values.append(str(d[key])

#print(count_digits_in_dict({1: 1234, 2: 2222, 3: 43234}, 4))