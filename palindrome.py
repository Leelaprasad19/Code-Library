def isPalindrome(string):
    
    if(string==string[::-1]):
        
        print(string)
        

n = int(input())

strings = input().split()

for string in strings:
    
    isPalindrome(string)
