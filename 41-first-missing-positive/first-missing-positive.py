class Solution(object):
    def firstMissingPositive(self, nums):
        nums=sorted(set(nums))
        counter=0
        for i in nums:
            if i >0 :
                counter+=1
                if i != counter :
                    return counter
        return counter+1