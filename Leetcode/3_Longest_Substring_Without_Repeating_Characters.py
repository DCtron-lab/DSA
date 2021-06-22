class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        
        max_length = start = end = 0
        map = {}
        
        
        while end < len(s):
            if s[end] in map and start <= map[s[end]]:
                start = map[s[end]] +1
            max_length = max(max_length, end - start+1)
            map[s[end]]=end
            end +=1
        return max_length
        