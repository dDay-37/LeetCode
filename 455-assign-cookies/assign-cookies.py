class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i=0
        j=0
        c=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
                j+=1
            i+=1
        return c