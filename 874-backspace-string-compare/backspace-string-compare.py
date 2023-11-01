class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = []
        b = []
        for x in s:
            if x == "#":
                if len(a) != 0:
                    a = a[:-1]
            else:
                a.append(x)
        for y in t:
            if y == "#":
                if len(t) != 0:
                    b = b[:-1]
            else:
                b.append(y)
        print(a)
        print(b)
        if a == b:
            return True
        else:
            return False
        