# cook your dish here


for i in range(int(input())):
    
    items,cost = list(map(int, input().split()))
    
    c = items//3
    
    rem = items - c * 3
    
    myCost = cost * 2 * c + rem * cost
    
    print(myCost)