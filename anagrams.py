from itertools import combinations
from math import *

def substrings(string):
    
    res = [''.join(sorted(string[x:y])) for x, y in combinations(range(len(string) + 1), r = 2)]
    
    res.sort()
    return res
 
def printNcR(n, r):
    p = 1
    k = 1
 
    if (n - r < r):
        r = n - r
 
    if (r != 0):
        while (r):
            p *= n
            k *= r
 
            m = gcd(p, k)
 
            p //= m
            k //= m
 
            n -= 1
            r -= 1
 
    else:
        p = 1

    return p


def anagram(s):
    
    sol = 0
    c = 0
    prev = s[0]
    for i in s: 
        if(i==prev):
            c+=1
        else:
            if(c > 2):
                sol += printNcR(c,2)
            elif(c==2):
                sol+=1
                
            prev = i
            c = 1
    
    if(c > 2):
        sol += printNcR(c,2)
    elif(c==2):
        sol+=1
        
    return sol
        
    
n = int(input())

# print("Hello")

for i in range(n):
    s = input()
    s = substrings(s)
    s.sort()
    
    # print(s)
    print(anagram(s))
    
