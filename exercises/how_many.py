def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    i = 0
    for value in aDict:
        if type(aDict[value]) == list:
            for item in aDict[value]:
                i = i + 1
        else: 
            i = i + 1
    return (i)
