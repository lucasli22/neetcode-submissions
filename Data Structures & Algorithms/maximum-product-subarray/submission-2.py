class Solution:
    def maxProduct(self, nums: List[int]) -> int:  
        if len(nums) < 2:
            return nums[0]

        currMax = nums[0]
        currMin = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            prevMax = currMax
            prevMin = currMin
            currMax = max(nums[i] * prevMax, nums[i] * prevMin, nums[i])
            currMin = min(nums[i] * prevMax, nums[i] * prevMin, nums[i])
            print(currMax, currMin)
            ans = max(currMax, ans)        
        return ans