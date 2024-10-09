from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o=0
        t=0
        for i in s:
            if i=='(':
                o+=1
                t+=1
            else:
                if o>0:
                    o-=1
                    t-=1
                else:
                    t+=1
        return t