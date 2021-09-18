class Solution(object):
    def sortColors(self, nums):
        p0, p, p2 = 0, 0, len(nums)-1
        while p <= p2:
            if nums[p] == 0:
                nums[p], nums[p0] = nums[p0], 0
                p0, p = p0 +1, p+1
            elif nums[p] == 2:
                nums[p], nums[p2] = nums[p2], 2
                p2 -= 1
            else:
                p+=1
            