def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    mutated_L = L[:]
    for item in mutated_L:
        if not g(f(item)):
            L.remove(item)
    if L != []:
        max_value = max(L)
    else:
        max_value = -1
    return max_value
