class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if num - 1 not in seen:
                curr = num + 1
                count = 1

                while curr in seen:
                    count += 1
                    curr += 1
                longest = max(count, longest)

        return longest