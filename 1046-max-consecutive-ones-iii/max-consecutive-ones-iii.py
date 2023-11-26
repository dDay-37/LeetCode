class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ind=[]
        c,i,j,m,n=0,0,0,0,len(nums)
        while j<n:
            # print(i,j,c,m)
            if nums[j]==1:
                j+=1
            elif k==0:
                i=j+1
                j+=1
                continue
            else:
                if c<k:
                    c+=1
                    ind.append(j)
                    j+=1
                elif ind:
                    i=ind[0]+1
                    ind=ind[1:]
                    c-=1
            m=max(m,j-i)
        return m