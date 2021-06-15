class Solution(object):
    def isAnagram(self, s, t):
            s = list(s)
            t = list(t) 
            s = sorted(s)
            t = sorted(t)  
            if len(s)==len(t):
                if s==t:
                    return True
                else:
                    return False
            else:
                return False 