'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
'''

count = 0
vowels = ["a", "e" , "i" , "o", "u"]
for i in range (len(s)):
    if s[i] in vowels:
        count = count + 1
print("Number of vowels: " + str(count))
