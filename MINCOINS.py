# cook your dish here



for i in range(int(input())):
    
    cost = int(input())
    
    if(cost%5!=0):
        print(-1)
    else:
        coins = cost//10
        coins += (cost - coins*10)//5
        print(coins)