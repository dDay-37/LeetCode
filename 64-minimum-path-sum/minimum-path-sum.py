class Solution:
    def minPathSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        dp=[[-1]*m for _ in range(n)]
        dp[0][0]=mat[0][0]
        for x in range(1,m):
            dp[0][x]=mat[0][x]+dp[0][x-1]
        for y in range(1,n):
            dp[y][0]=mat[y][0]+dp[y-1][0]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=mat[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]