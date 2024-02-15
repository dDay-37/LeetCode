class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # Sort the list in ascending order
        Csum = Psum = 0  # Initialize current sum and perimeter sum to 0

        for i in range(len(nums)):
            # Check if the current element can be part of a valid triangle
            if nums[i] < Csum:
                Psum = Csum + nums[i]  # Update perimeter sum with the potential triangle's perimeter
            Csum += nums[i]  # Update current sum with the current element

        # Return the largest perimeter if a valid triangle is found, otherwise return -1
        return -1 if Psum == 0 else Psum