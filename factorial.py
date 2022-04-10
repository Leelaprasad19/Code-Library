def factorial(n):
    
    fact = 1
      
    for i in range(1,n+1):
        fact = fact * i
          
    print ("The factorial of 23 is : ",end="")
    # print (fact)

for i in range(1,400):
    
    factorial(i)