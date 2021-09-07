class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result = []
        start,end = intervals[0][0],intervals[0][1]
        for i in intervals:
            if i[0] > end: #no overlap
                result.append([start, end])
                start, end = i[0], i[1]
            else: #overlap
                 end = max(end, i[1])
        result.append([start, end]) 
        return result