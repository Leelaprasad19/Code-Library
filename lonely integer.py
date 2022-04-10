def lonelyinteger(a):

    sol = 0
    for i in a:
        sol = sol ^ i
    return sol 

arr = [1,2,3,2,4,3,1]
print(lonelyinteger(arr))