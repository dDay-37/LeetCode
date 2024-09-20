class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        # at this point, everything in s[j:] is part of our suffix, and s[:j] contains a palindrome within it
        if j == len(s):  # this can only occur if the entire string s was a palindrome. If so, we are done!
            return s
        # otherwise, keep working on s[:j] to verify how much of it is a palindrome, and place prefix and suffix around it.
        # the recursion works because if j != len(s), then we are always recursing into a shorter and more palindrome-ish string.
        return s[j:][::-1] + self.shortestPalindrome(s[:j]) + s[j:]  