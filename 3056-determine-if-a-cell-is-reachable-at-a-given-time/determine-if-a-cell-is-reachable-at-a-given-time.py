class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        a = 0 
        a += min(abs(fx - sx), abs(fy - sy))
        if fy - sy > 0:
            sy += a
        else:
            sy -= a 
        if fx - sx > 0:
            sx += a  
        else:
            sx -= a  
        a += max(abs(fx - sx), abs(fy - sy))
        if a == 0 and t == 1:  
            return False
        if a <= t: 
            return True
        return False