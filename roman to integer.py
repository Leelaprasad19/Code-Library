def romanToInt(s):
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        l = len(s)
        
        if(l==1):
            return d[s]
        
        num_ = 0
        for i in range(1,l):
            if(d[s[i]] <= d[s[i-1]]):
                num_ += d[s[i-1]]
            else:
                num_ -= d[s[i-1]]
        
        num_ += d[s[-1]]
        
        return num_
      
