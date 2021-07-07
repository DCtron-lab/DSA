class Solution(object):
    def isValid(self, s):
        if len(s)%2 == 1:
            return False
        arr = []
        braces = {"{":"}","[":"]","(":")"}
        
        for c in s:
            if c in braces:
                arr.append(c)
            elif len(arr) != 0 and c == braces[arr[-1]]:
                arr.pop()
            else:
                return False
            
        return len(arr) == 0
        