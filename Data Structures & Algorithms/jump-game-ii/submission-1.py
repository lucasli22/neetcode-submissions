class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0
        while r < len(nums) - 1:
            currMax = 0 
            for i in range(l, r + 1):
                currMax = max(currMax, nums[i])
            r += currMax
            l += 1
            steps += 1
        return steps




        