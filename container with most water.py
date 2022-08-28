def maxArea(height):
        
        n = len(height)
        
        i = 0
        j = n-1
        sol = 0
        while(i < j):
            if(height[i] < height[j]):
                a = height[i] * (j - i)
                i = i + 1
            else:
                a = height[j] * (j - i)
                j = j - 1
                
            if(a > sol):
                sol = a
        
        return sol
        
