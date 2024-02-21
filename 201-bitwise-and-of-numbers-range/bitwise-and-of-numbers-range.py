class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right == 0:#in this case, left,right = 0,0
            return 0

        #find the biggest power of 2 less than or equal to right
        closest_power_of_2 = 2**floor(log(right, 2))

        
        if left < closest_power_of_2:
            return 0
        if left == closest_power_of_2:
            return closest_power_of_2
        return self.rangeBitwiseAnd(left - closest_power_of_2, right - closest_power_of_2) + closest_power_of_2