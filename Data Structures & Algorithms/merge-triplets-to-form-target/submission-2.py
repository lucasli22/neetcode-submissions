class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        aMax = 0
        bMax = 0
        cMax = 0
        for a, b, c in triplets:
            
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            aMax = max(aMax, a)
            bMax = max(bMax, b)
            cMax = max(cMax, c)
            if aMax == target[0] and bMax == target[1] and cMax == target[2]:
                return True
        return False