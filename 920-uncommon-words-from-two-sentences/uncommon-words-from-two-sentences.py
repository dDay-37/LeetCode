class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        x=s1+" "+s2
        x=x.split()
        c=Counter(x)
        ans=[]
        for i in c:
            if c[i]==1:
                ans.append(i)
        return ans