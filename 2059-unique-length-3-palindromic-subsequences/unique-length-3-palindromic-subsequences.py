class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for i in set(s):
                start, end = s.find(i), s.rfind(i)
                between = set(s[start+1:end])
                count += len(between)
        return count