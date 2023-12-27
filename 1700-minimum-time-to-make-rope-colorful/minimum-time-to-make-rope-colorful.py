class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        id=[]
        colors=list(colors + "0")
        print(colors)
        curr=colors[0]
        ci=0
        s=0
        for i in range(1,len(colors)):
            if colors[i]!=curr:
                # print(colors[ci:i])
                s+=sum(neededTime[ci:i])- max(neededTime[ci:i])
                ci=i
                curr=colors[i]
        return s