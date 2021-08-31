'''
 Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). 
 The list of keys you return should be sorted in increasing order. 
 If aDict does not contain any unique values, you should return an empty list.

This function takes in a dictionary and returns a list.
'''

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    unique_keys = []
    for key, value in aDict.items():
        i = 0
        for k, v in aDict.items():
            if value == v:
                i = i + 1
        if i == 1: 
            unique_keys.append(key)
    return unique_keys
  
### Test: uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0})
### Test: uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0})
