class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):  # Function definition

        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        a = 0  # Initialize the time taken to travel
        a += min(abs(fx - sx), abs(fy - sy))  # Calculate and add the time taken to cover the minimum distance

        if fy - sy > 0:  # If the y coordinate difference is positive
            sy += a  # Update sy by adding the value of a
        else:
            sy -= a  # Otherwise, update sy by subtracting the value of a

        if fx - sx > 0:  # If the x coordinate difference is positive
            sx += a  # Update sx by adding the value of a
        else:
            sx -= a  # Otherwise, update sx by subtracting the value of a

        a += max(abs(fx - sx), abs(fy - sy))  # Calculate and add the time taken to cover the remaining distance

        if a == 0 and t == 1:  # If a is 0 and t is 1, return False
            return False

        if a <= t:  # If a is less than or equal to t, return True
            return True

        return False  # Otherwise, return False