class Solution:
    def hammingWeight(self, n: int) -> int:
    
            c = 0
            for bit in range(32):
                if n & (1<<bit):
                    c += 1
                    
            return c 