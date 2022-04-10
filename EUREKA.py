# https://www.codechef.com/viewsolution/57727384
import math as m

n = int(input())

for i in range(n):
    
    t = int(input())
    
    sol = (0.143 * t)**t
    
    temp = sol - m.floor(sol)
    
    if(temp < 0.5):
        sol = int(sol)
    else:
        sol = int(sol) + 1
    
    print(sol)