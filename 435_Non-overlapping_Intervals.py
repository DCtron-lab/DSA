class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) < 2: return 0
        
        intervals.sort(key= lambda x:x[1])
        remove = 0
        end = intervals[0][0]
        for times in intervals:
            start = times[0]
            if start < end:
                remove += 1
            else:
                end = times[1]
        return remove