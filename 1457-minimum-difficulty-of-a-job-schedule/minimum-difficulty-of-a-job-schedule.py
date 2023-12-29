class Solution:
    def minDifficulty(self, jD: List[int], d: int) -> int:
        if len(jD)<d:return -1
        dp=[[0 for i in range(d+1)] for i in range(len(jD)+1)]
        for i in range(d+1):dp[len(jD)][i]=10**6
        for i in range(len(jD)):dp[i][1]=max(jD[i:])
        for i in range(len(jD)-1,-1,-1):
            for j in range(2,d+1):
                ans,mx=10**6,-1
                for k in range(i,len(jD)):
                    mx=max(mx,jD[k])
                    temp=mx+dp[k+1][j-1]
                    ans=min(ans,temp)
                dp[i][j]=ans
        return dp[0][d]