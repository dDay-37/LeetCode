class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mat=[[]]
        for i in nums:
            f=0
            for j in mat:
                if i not in j:
                    j.append(i)
                    f=1
                    break
            if f==0:
                mat.append([i])
        return mat        