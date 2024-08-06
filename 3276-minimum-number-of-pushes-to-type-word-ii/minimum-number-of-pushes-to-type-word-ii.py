class Solution:
    def minimumPushes(self, word: str) -> int:
        s=dict(Counter(word))
        # print(s)
        s0=sorted(s,key=lambda x:s[x],reverse=True)
        # print(s0)
        c=0
        for i in range(len(s0)):
            c+=s[s0[i]]*(i//8 +1)
        return c