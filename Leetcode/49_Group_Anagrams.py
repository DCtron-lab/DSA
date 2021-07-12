class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        m={}
        for st in strs:
            s=''.join(sorted(st))
            if s in m.keys():
                m[s].append(st)
            else:
                m[s]=[st]
        for s in m:
            ans.append(m[s])
        return ans