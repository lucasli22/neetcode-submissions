class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        def rec(n):
            if n < 0:
                return
            if dp[n] != 1:
                return dp[n]
            for i in range(n, len(nums)):
                if nums[n] < nums[i]:
                    print("YAYAYA", n, i)
                    dp[n] = max(dp[n], 1 + dp[i])
            
            rec(n-1)
            return dp[n]

        rec(len(nums) - 1)
        print(dp)
        return max(dp)
                
