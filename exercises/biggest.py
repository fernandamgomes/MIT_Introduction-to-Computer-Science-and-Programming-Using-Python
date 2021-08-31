def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggest_key = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggest_key:
            biggest_key = len(aDict[key])
            result = key
    return(result)
