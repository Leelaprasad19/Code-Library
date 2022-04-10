def function():
    
    correct = 0
    incorrect = 0
    
    questions, marks = list(map(int, input().split()))
    
    
    if(marks%3==0):
        correct = marks//3
    elif(marks%3==1):
        correct = marks//3 + 1
        incorrect = 2
    else:
        correct = marks//3 + 1
        incorrect = 1
        
    if(correct+incorrect > questions):
        print("NO")
    else:
        print("YES")
        print(correct,incorrect,questions-correct-incorrect)
        

for i in range(int(input())):
    function()

