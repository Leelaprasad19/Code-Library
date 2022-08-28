def lengthOfLongestSubstring(s):
        
        sub = ""
        max_ = 0
        l = 0
        for i in s:
            if(i not in sub):
                sub += i
                l += 1
                if(l > max_):
                    max_ = l
            else:
                x = sub.find(i)
                sub = sub[x+1:] + i
                l -= x
                print(sub,l)
                
        return max_
        
