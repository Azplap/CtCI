import timeit
from collections import defaultdict
# Bottlenecks

"""
Example: Given an array of distinct integer values,
count the number of pairs of integers that have difference k.
For example, given the array { 1,  7,  5,  9,  2,  12,  3} and
the difference k =  2,thereare four pairs with difference 2:
(1,  3),  (3,  5),  (5,  7),  (7, 9).

"""
# bruteforce
# check each number with every subsequent number
# loop across full list but check a spliced version of the list w/ enumerate
# so it's slightly better than checking every number against every numbe
# runtime: n * (n-1) * (n-2)... 1, looks like O(n2)

l=[1,  7,  5,  9,  2,  12,  3]

def diff_bruteforce(l):
    pairs=[]
    for n, x in enumerate(l):
        for y in l[n:]:
            if abs(x-y)==2:
                pairs.append((x,y))

    return pairs

# first time through, didn't read carefully!
# we're counting the number of pairs, so we should return 4.
# I'll use a defaultdict (hashtable) to do it efficiently
# count the number of x+-y==K for each x
# then find sum of values

def diff_hash(l):
    dd=defaultdict()
    for x in l:
        print(x)
        dd.update(x)
    print(dd)
    return

if __name__ == "__main__":
    diff_hash(l)
