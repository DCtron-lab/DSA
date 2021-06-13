    class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length=0
        freq=0
        start=0
        charset={}
        
        for end in range(len(s)):
            print(start,end)
            curr = s[end]
            if curr not in charset:
                charset[curr]=1
            else:
                charset[curr]+=1
                
            freq=max(freq,charset[curr])
            
            length=end-start+1
            
            if length-freq <= k:
                max_length=max(max_length,length)
            else:
                charset[s[start]]-=1
                start+=1
            
        return max_length