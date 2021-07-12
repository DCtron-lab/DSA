class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        m=max(nums)
        if m<0:
            return 1
        for i in range(1,m+2):
            if i not in nums:
                return i