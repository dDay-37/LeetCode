class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        # print(a)
        t=0
        for i in words:
            t+=1
            for l in i:
                if l not in a:
                    t-=1
                    break
        return t