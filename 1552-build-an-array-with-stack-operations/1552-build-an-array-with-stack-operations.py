class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        last = target[-1]
        i=1
        j = 0
        while i<last+1:
            ans.append("Push")
            if i == target[j]:
                j+=1
            else:
                ans.append("Pop")
            i+=1
        return ans