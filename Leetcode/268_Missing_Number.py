class Solution(object):
    def missingNumber(self, nums):
        x = len(nums) 
        for i in range(len(nums)):
            x = x^nums[i]
            x = x^i
        return x