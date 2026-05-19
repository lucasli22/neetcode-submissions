class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            num = nums[i]
            if currSum + num < 0:
                maxSum = max(maxSum, num)
                currSum = 0
            else:
                currSum += num
                maxSum = max(maxSum, currSum)
            print(currSum, maxSum, num)
        return maxSum

