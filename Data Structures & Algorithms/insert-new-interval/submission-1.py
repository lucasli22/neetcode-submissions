class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        start = newInterval[0]
        end = newInterval[1]

        i = 0
        curl = start
        curr = end 
        inserted = False
        while i < len(intervals):
            l = intervals[i][0]
            r = intervals[i][1]
            
            if inserted:
                ans.append([l, r])
            else:
                if l > curr:
                    ans.append([curl, curr])
                    ans.append([l, r])
                    inserted = True
                elif r < curl:
                    ans.append([l, r])
                else:
                    curl = min(l, curl)
                    curr = max(r, curr)
            
            i += 1
        if not inserted:
            ans.append([curl, curr])
        return ans
            # if r < start or l > end:
            #     if prel and prer:
            #         ans.append([prel, prer])
            #         prel, prer = None, None
            #     ans.append([l, r])
            # else:
            #     if not prel: 
            #         prel = l
            #     else:
            #         prel = min(start, l)
            #     if not prer:
            #         prer = r
            #     else:
            #         prer = max(end, r)
        #     i += 1
        # if prel and prer:
        #     ans.append([prel, prer])
        # return ans

