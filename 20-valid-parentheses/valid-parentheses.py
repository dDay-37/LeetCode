class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[0]
        for i in s:
            l.append(i)
            if i==")":
                if l[-2]=="(":
                    l.pop()
                    l.pop()
                else:
                    return False
            if i=="}":
                if l[-2]=="{":
                    l.pop()
                    l.pop()
                else:
                    return False
            if i=="]":
                if l[-2]=="[":
                    l.pop()
                    l.pop()
                else:
                    return False
        print("l",l)
        if len(l)==1:
            return True
        else:
            return False