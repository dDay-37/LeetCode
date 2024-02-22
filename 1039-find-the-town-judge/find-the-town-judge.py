class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)<n-1:
            return -1
        itrust=[0]*n
        trustedby=[0]*n
        for i in trust:
            itrust[i[0]-1]+=1
            trustedby[i[1]-1]+=1
        for i in range(n):
            if itrust[i]==0 and trustedby[i]==(n-1):
                return i+1
        return -1