class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        ans = 0 
        for currStart, currEnd in intervals[1:]:
            if currStart < end:
                ans += 1
                end = min(end, currEnd)
            else:
                end = currEnd
        return ans
                