class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)<n-1:
            return -1
        x=[0]*n
        for (a,b) in trust:
            x[a-1]-=1
            x[b-1]+=1
        for i in range(n):
            if x[i]==n-1:
                return i+1
        return -1
