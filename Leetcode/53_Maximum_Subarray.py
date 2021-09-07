class Solution(object):
    def maxSubArray(self, nums):
        max_nums = max(nums)
        if max_nums < 0:
            return max_nums
        
        cur_sum = 0
        max_sum = 0
         
        for num in nums:
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
        