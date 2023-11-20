class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        s=0
        travel.append(0)
        m,p,g=0,0,0
        for i in range(len(garbage)):
            m+=travel[i-1]
            p+=travel[i-1]
            g+=travel[i-1]
            if "M" in garbage[i]:
                s+=m+garbage[i].count('M')
                m=0
                # print(garbage[i],garbage[i].count('M'))
            if "P" in garbage[i]:
                s+=p+garbage[i].count('P')
                p=0
                # print(garbage[i],garbage[i].count('P'))
            if "G" in garbage[i]:
                s+=g+garbage[i].count('G')
                g=0
                # print(garbage[i],garbage[i].count('G'))
        return s
