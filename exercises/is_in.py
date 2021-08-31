def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # If the length of the string is 0, char can't be in it
    if len(aStr) == 0:
        return False
    # Base case: if length = 1 and the char doesn't match what's left of the string -> False
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char:
        return True
    else:
        if aStr[len(aStr)//2] > char:
            return isIn(char, aStr[0 : len(aStr)//2])
        elif aStr[len(aStr)//2] < char:
            return isIn(char, aStr[len(aStr)//2 + 1 : len(aStr)])
