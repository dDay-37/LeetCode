class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []

        for num in nums:
            found = False
            for group in res:
                if num in group:
                    continue
                else:
                    found = True
                    group.add(num)
                    break
            
            if not found:
                res.append(set([num]))
        
        return res
            
        