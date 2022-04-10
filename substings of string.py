from itertools import combinations

def substrings(string):
    
    res = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]
    
    return res

string = input('Enter Input : ')

res = substrings(string)
  
print("All substrings of string are : \n",res)