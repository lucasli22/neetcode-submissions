class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        ans = 0 
        for currStart, currEnd in intervals[1:]:
            if currStart < end:
                if currEnd < end:
                    ans += 1
                    end = currEnd
                    currStart = start
                else:
                    ans += 1        
            else:
                start = currStart
                end = currEnd
        return ans
                