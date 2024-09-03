class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s=list(s)
        for i in range(len(s)):
            s[i]=str(ord(s[i])-96)
        # print(s)
        s="".join(s)
        for x in range(k):
            v=0
            for d in s:
                v+=int(d)
            s=str(v)
        return int(s)