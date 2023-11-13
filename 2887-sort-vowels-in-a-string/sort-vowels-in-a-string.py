class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=[]
        a=[]
        vo=['a','e','i','o','u']
        for i in s:
            if i.lower() in vo:
                v.append(i)
        v.sort()
        z=0
        for i in s:
            if i.lower() not in vo:
                a.append(i)
            else:
                a.append(v[z])
                z+=1
        return "".join(a)

