class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        lo = 1
        hi = max(piles)
        ans = hi
        def canFinish(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            
            if time > h:
                return False
            else:
                return True
        
        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                ans = mid
                hi = mid
            else:
                lo = mid + 1

        return ans