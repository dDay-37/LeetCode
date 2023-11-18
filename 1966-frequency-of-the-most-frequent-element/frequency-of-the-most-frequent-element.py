class Solution:
    def maxFrequency(self, nums, k):
        self.customSort(nums)
        start = 0
        sub_sum = 0
        max_freq = 1

        for i in range(len(nums)):
            sub_len = i - start + 1
            sub_prod = nums[i] * sub_len
            sub_sum += nums[i]

            while sub_prod - sub_sum > k:
                sub_sum -= nums[start]
                start += 1
                sub_len -= 1
                sub_prod = nums[i] * sub_len

            max_freq = max(max_freq, sub_len)

        return max_freq

    def customSort(self, nums):
        max_elem = max(nums)
        count_map = [0] * (max_elem + 1)

        for num in nums:
            count_map[num] += 1

        index = 0

        for i in range(max_elem + 1):
            while count_map[i] > 0:
                nums[index] = i
                index += 1
                count_map[i] -= 1