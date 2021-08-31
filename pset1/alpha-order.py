'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. In the case of ties, print the first substring.

For example, if s = 'azcbobobegghakl', then your program should print:

"Longest substring in alphabetical order is: abc"Longest substring in alphabetical order is: beggh
'''

i = 0
temp_str = s[i]
list_str = []
for i in range (len(s) - 1):
    if (ord(s[i])) < (ord(s[i+1])) or (ord(s[i])) == (ord(s[i+1])):
        temp_str = temp_str +  s[i+1]
    else:
        list_str.append(temp_str)
        temp_str = s[i+1]
list_str.append(temp_str)
longest_str = max(list_str, key=len)
print("Longest substring in alphabetical order is: " + longest_str)
