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
        if sx == fx and sy == fy:
            if t == 1:
                return False
            else:
                return True
        return abs(sx - fx) <= t and abs(sy - fy) <= t