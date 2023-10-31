class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        l,r,ans=0,len(height)-1,0
        lmax,rmax = height[l],height[r]

        while l<r:
            if lmax<rmax:
                water = lmax - height[l]
                l+=1
                lmax = max(lmax,height[l])
            else:
                r-=1
                water = rmax - height[r]
                rmax = max(rmax,height[r])
            if water>0:
                ans+=water
        return ans