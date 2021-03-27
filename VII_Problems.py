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
k=2
def diff_bruteforce(l, k):
    pairs=[]
    for n, x in enumerate(l):
        for y in l[n:]:
            if abs(x-y)==k:
                pairs.append((x,y))

    return pairs

# first time through, didn't read carefully!
# we're counting the number of pairs, so we should return 4.
# I'll use a defaultdict (hashtable) to do it efficiently
# count the number of x+-y==K for each x
# then find sum of values

def diff_hash(l, k):
    dd=defaultdict(int)
    for x in l:
        # checks to see if the pair already exists as well
        if (x+k in l and dd[x+k]) or (x-k in l and dd[x-k]):
            dd[x]+=1
    print(dd)

    return sum(dd.values())

if __name__ == "__main__":
    ans=diff_hash(l, k)
    print(ans)
