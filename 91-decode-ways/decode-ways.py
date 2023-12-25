class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_2 = 1
        dp_1 = int(s[-1] != "0")

        i = len(s) - 2
        while i >= 0:
            if s[i] == "0":
                dp_0 = 0
            else:
                dp_0 = dp_1
                if (s[i] == "1") or (s[i] == "2" and eval(s[i + 1]) < 7):
                    dp_0 += dp_2
            i -= 1
            dp_0, dp_1, dp_2 = 0, dp_0, dp_1
        
        return dp_1