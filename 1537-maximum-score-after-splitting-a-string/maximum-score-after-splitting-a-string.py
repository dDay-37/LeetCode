class Solution(object):
    def maxScore(self, s):
        one=0
        for i in range(1,len(s)):
            if s[i] == "1":
                one+=1
       
        if s[0] == "1":
            zero = 0
            res = one
        if s[0] == "0":
            zero = 1
            res = one +1
    
        for i in range(1,len(s)-1):
            
            if s[i] == "0":
                zero+=1
            if s[i] == "1":
                one-=1
            res = max(res, zero+one)
  
        return res