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
        
    values = []
    for key in d:
        values.append(str(d[key]))
    digits = []
    for value in values:
        for char in value:
            digits.append(char)
    times = 0
    for dig in digits:
        if dig == str(digit):
            times = times + 1
    return times
    

print count_digits_in_dict({1:1234, 2:2222, 3:43234},4)
print count_digits_in_dict({1:1234, 2:2222, 3:43234},0)