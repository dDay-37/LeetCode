class Solution(object):
    def maxScore(self, s):
        r = 0
        for i in range(len(s) - 1):
            c = 0
            for j in range(i + 1):
                if s[j] == '0':
                    c += 1
            for j in range(i + 1, len(s)):
                if s[j] == '1':
                    c += 1
            r = max(r, c)
        return r
