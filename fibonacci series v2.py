def fibonacciRec(i,n,a,b):
    
    if(i==0):
        print(a, end=' ')
        fibonacciRec(i+1,n,0,1)
    elif(i==1):
        print(b, end=' ')
        fibonacciRec(i+1,n,0,1)
    elif(i <= n):
        print(a+b, end=' ')
        fibonacciRec(i+1,n,b,a+b)

n = 50
fibonacciRec(1,n,0,1)
