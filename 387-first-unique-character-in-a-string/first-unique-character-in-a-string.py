class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=Counter(s)
        for i in a:
            if a[i] == 1:
                return s.index(i)
        return -1