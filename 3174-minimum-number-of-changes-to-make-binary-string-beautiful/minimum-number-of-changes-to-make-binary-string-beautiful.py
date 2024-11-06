class Solution:
    def minChanges(self, s: str) -> int:
        return sum(map(ne,*[iter(s)]*2))