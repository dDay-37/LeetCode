
class Solution(object):
    def gcd(self, x, y):
        if (y == 0):
            return x
        else:
            return self.gcd(y, x % y)  
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:self.gcd(len(str1), len(str2))]
