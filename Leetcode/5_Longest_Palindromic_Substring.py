class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        max_len = 1
        n = len(s)
        st, end = 0, 0
        
        # Odd length
        for i in range(n-1):
            l, r = i, i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l, r = l-1, r+1
                else:
                    break
            _len = r-l-1
            if _len > max_len:
                max_len = _len
                st, end = l+1, r-1
        
        # Even length
        for i in range(n-1):
            l, r = i, i+1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l, r = l-1, r+1
                else:
                    break
            _len = r-l-1
            if _len > max_len:
                max_len = _len
                st, end = l+1, r-1
        
        return s[st:end+1]