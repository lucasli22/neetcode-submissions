class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * (len(nums)+1) for _ in range(len(nums))] 
        def rec(n, prevIdx):
            if n == len(nums):
                return 0
            if dp[n][prevIdx+1] != -1:
                return dp[n][prevIdx+1]
            if prevIdx == -1 or nums[n] > nums[prevIdx]:
                
                dp[n][prevIdx+1] = 1 + rec(n+1, n)

            dp[n][prevIdx+1] = max(dp[n][prevIdx+1], rec(n+1, prevIdx))
                

            return dp[n][prevIdx+1]
        
        return rec(0, -1)
              
        
        