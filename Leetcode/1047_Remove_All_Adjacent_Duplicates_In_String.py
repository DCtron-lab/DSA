class Solution(object):
    def removeDuplicates(self, S):
        st =[]
        for c in S:
            if len(st) > 0 and st[-1] == c:
                st.pop()
            else:
                st.append(c)
        return "".join(st)
        
        