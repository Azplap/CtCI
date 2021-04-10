from collections import defaultdict

"""
1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
# first impression: create a temp array and check against it for each characters
# pretty simply, something like O(nlogn)
def one_one(str):
    temp=[]
    for c in str:
        if c in temp:
            return False
        else:
            temp.append(c)
    return True
# not sure how to do this w/o additional data structures
# a hashtable would improve runtime to O(n)
def one_one_improvement(str):
    d=defaultdict(int)
    for c in str:
        if d[c]>=1:
            return False
        else:
            d[c]+=1
    return True

"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""
# first of all, they'll have to be the same size - base case check that
# if same size, check and see if the number of occurences is the same for each char
# fill two dicts and check if they match. runtime O(2n)
def one_two(str1, str2):
    if len(str1) != len(str2):
        return False
    d1,d2=defaultdict(int), defaultdict(int)
    for x in str1:
        d1[x]+=1
    for x in str2:
        d2[x]+=1
    if d1 == d2:
        return True
    else:
        return False

"""
1.3 URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters, and that you are given the "true" length of the string.
"""
# loop through string: if char is a space append %20
# else: append char. Join array at the end. Runtime O(n)
# base case if None retun none.
def one_three(str):
    if not str:
        return None
    ans=[]
    for x in str:
        if x == ' ':
            ans.append('%20')
        else:
            ans.append(x)
    return ''.join(ans)
"""
1.4 Palindrome Permutation: Given a string, write a function to check if it
is a permutation of a palin­drome. A palindrome is a word or phrase that is
the same forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.
"""
# We want to see if the characters in the string can be rearranged into
# a palindrome. First 'hard one'.
# Could come up w/ all permutations and then check if the reverse of each is True
# Thats a solution, but it's giga inefficient.

"""
1.5 One Away: There are three types of edits that can be performed on strings:
 insert a character, remove a character, or replace a character.
 Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
# could check each of the three edits
# or instead use the hash table again and see how many
# differences there are for each character
def one_five(str1, str2):
    d1,d2=defaultdict(int),defaultdict(int)
    for x in str1:
        d1[x]+=1
    for x in str2:
        d2[x]+=1
    differences=0
    for x in d1.keys():
        differences+= abs(d1[x] - d2[x])



if __name__ == '__main__':
    ans = one_three(' ')
    print(ans)
