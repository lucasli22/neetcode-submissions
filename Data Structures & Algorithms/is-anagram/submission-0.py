class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        sCount = Counter(list(s))
        tCount = Counter(list(t))

        return sCount == tCount