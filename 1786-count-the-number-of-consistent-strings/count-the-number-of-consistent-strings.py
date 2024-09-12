class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        # print(a)
        c=0
        for i in words:
            for l in i:
                if l not in a:
                    c+=1
                    break
        return len(words)-c