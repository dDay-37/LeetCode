class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        # print(k)
        for i in range(len(chalk)):
            if chalk[i]<=k:
                k-=chalk[i]
            else:
                return i
        return len(chalk)-1
        