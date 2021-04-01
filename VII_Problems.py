import timeit
from collections import defaultdict
from tqdm import tqdm

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
# runtime: O(n), just passes through list once!
def diff_hash(l, k):
    dd=defaultdict(int)
    for n,x in enumerate(l):
        # checks to see if the pair already exists as well
        if (x+k in l and dd[x+k]==0):
            dd[x]+=1
        if (x-k in l and dd[x-k]==0):
            dd[x]+=1
    print(dd)

    return sum(dd.values())



"""
Example: Print all positive integer solutions to the equation a3 + b3 = c3 +d3
where a, b, c, and d are integers between 1 and 1000.
"""
# brutforce first
# the classic quadruple for loop
# should be right though...
# update: yikes

n=range(1,1000)
def findNums_bruteforce():
    solutions=[]
    for a in tqdm(n):
        for b in n:
            for c in n:
                for d in n:
                    if (a^3 + b^3) == (c^3 + d^3):
                        solutions.append((a,b,c,d))
    return solutions


# okay... optimizations!
#



if __name__ == "__main__":
    # ans=diff_hash(l, k)
    # print(ans)

    # ans=findNums_bruteforce()
    # print(ans)
    for x in tqdm(range(0,10000)):
        pass
