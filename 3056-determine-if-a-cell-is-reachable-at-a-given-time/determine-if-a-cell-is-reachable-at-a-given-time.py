class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        a=0
        a+=min(abs(fx-sx),abs(fy-sy))
        # print("a",a)
        if fy-sy>0:
            sy+=a
        else:
            sy-=a
        if fx-sx>0:
            sx+=a
        else:
            sx-=a
        # print(sx,sy)
        a+=max(abs(fx-sx),abs(fy-sy))
        # print("a",a)
        if a==0 and t==1:
            return False
        if a<=t:
            return True
        return False