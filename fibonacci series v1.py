def fibonacci(n):
    a = 0
    b = 1
     
    if n < 0:
        print("Incorrect input")
         
    elif n == 0:
        return 0
       
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(c)
        return b

n = int(input('Enter number of fibonacci numbers - '))
fibonacci(n)
