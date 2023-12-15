class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        c=paths[0][1]
        s=[]
        d=[]
        for i in paths:
            s.append(i[0])
            d.append(i[1])
        for j in d:
            if j not in s:
                return j