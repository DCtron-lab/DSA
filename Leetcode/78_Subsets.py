class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0: return [[]]
        result = [[]]
        
        for x in nums:
            n = len(result)
            for i in range(n):
                r = result[i] + [x]
                result.append(r)
                
        return result    