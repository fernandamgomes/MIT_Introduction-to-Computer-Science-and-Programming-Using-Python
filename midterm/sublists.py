'''
Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.
  - assume L is not empty
  - assume 0 < n <= len(L)

This function returns a list of all possible sublists in L of length n without skipping elements in L. 
The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.
'''

def getSublists(L, n):
    sublists = []
    for i in range (len(L)):
        if i + n <= (len(L)):
            list_n = L[i:i+n]
            sublists.append(list_n)
    return(sublists) 
