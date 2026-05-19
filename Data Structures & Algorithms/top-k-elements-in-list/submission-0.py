class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        res = []
        for num, count in freq.most_common(k):
            res.append(num)

        return res