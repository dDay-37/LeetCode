class Solution:
    def findLength(self, n1: List[int], n2: List[int]) -> int:
        n=len(n1)
        m=len(n2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        # for row in dp:
        #     print(row)
        mx=0
        for i in range(1,m+1):
            # print("hi")
            for j in range(1,n+1):
                # print("there")
                # print(n1[i-1],n2[j-1])
                if n1[j-1]==n2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                #     print("hehe")
                #     print(n1[i-1],n2[j-1],dp[i][j])
                # print(i,j)
                # for row in dp:
                #     print(row)
                # print(dp[i][j])
                if dp[i][j]>mx:
                    mx=dp[i][j]
        # print("lala")
        # for row in dp:
        #     print(row)
        # print(n2[mi-mx:mi])
        return mx
