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
# A string that fits the bill would need to have an even number of
# most of its numbers w/ one odd, if the length is odd.
# Maybe I can run a mod check on the counts of each number.
def one_four(string):
    d=defaultdict(int)
    for x in string:
        if x !='':
            d[x]+=1
    if len(string)%2==0:
        # if string is even
        for value in d.values():
            if value%2 != 0:

                return False
    else:
        # if string is odd
        counter=0
        for value in d.values():
            if value%2 != 0:
                counter+=1
            if counter==1:
                return False
    return True

"""
***
1.5 One Away: There are three types of edits that can be performed on strings:
 insert a character, remove a character, or replace a character.
 Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
# could check each of the three edits or instead use the hash table again and see how many
# differences there are for each character. Boils down to too many or too little of a char
# or if the character isn't even there. Technically O(n)
def one_five(str1, str2):
    d1,d2=defaultdict(int),defaultdict(int)
    for x in str1:
        d1[x]+=1
    for x in str2:
        d2[x]+=1
    differences=0
    if len(d1.keys()) > len(d2.keys()):
        larger = d1.keys()
    else:
        larger = d2.keys()
    for x in larger:
        differences+= abs(d1[x] - d2[x])
    return differences
"""
1.6 String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""
# looks like we're using another hashtable!
# don't have to walk through it b4 hand it seems prettys simple
# base case: no string or not String. Looks like str is the keyword for string type!
#
# uh oh didn't READ CAREFULLLLLLY!! Bad habit. Should only add consecutive.
# can loop once, and use a counter that resets, checks the prev iteration to see if
# it's the same. still O(n)
def one_six(string):
    # base case
    if type(string) != str or string==None:
        return None
    counter,prev,compressed=0,string[0],[]
    for character in string:
        # adds character and count after new character
        if character!=prev:
            compressed.extend([prev,str(counter)])
            prev=character
            counter=1
        # replaces prev AND increments count
        else:
            prev=character
            counter+=1
    # adds last char after string ends haha
    compressed.extend([prev, str(counter)])
    # check length
    print(compressed)
    if len(compressed)>len(string):
        return string
    else:
        return ''.join(compressed)

"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.Can you do this in place?
"""
# AHHH ANOTHER MATRIX ONE ITS BEEN TOO LONG
# pretty sure theres a really pythonic way to do this
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
def one_seven(matrix):
    new=[]
    for row in matrix[::-1]:
        for value in row:
            new.append(value)
    return new

if __name__ == '__main__':
    ans=one_four('Tact Coa')
    print(ans)
    # ans = one_seven(matrix)
    # print(ans)
