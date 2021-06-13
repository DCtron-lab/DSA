class Solution(object):
    def getSum(self, a, b):
        xor = a^b 
        carry = a&b
        return add(xor,carry<<1)
