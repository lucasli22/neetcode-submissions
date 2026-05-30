class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        currStart, currEnd = intervals[0][0], intervals[0][1]

        for start, end in intervals:
            if currEnd < start:
                ans.append([currStart, currEnd])
                currStart = start
                currEnd = end
            else:
                currEnd = max(currEnd, end)
        
        ans.append([currStart, currEnd])
        return ans
