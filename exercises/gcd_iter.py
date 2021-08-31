def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    div = 1
    temp_div = 1
    while (temp_div <= a) and (temp_div <= b):
        if (a % temp_div == 0) and (b % temp_div== 0):
            div = temp_div
        temp_div = temp_div + 1
    return div
