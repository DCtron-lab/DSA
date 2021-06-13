class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        
        def count(n):
            c = 0
            for bit in range(32):
                if n & (1<<bit):
                    c += 1
                    
            return c
        
        print(count(0), count(1), count(2))
        
        for i in range(num+1):
            ans.append(count(i))
            
        return ans