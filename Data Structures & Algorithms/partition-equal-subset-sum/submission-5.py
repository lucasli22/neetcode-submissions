class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if total % 2 != 0:
            return False
        dp = [[None] * (half + 1) for _ in range(len(nums))]
        def rec(n, currSum) -> bool:
            if n == len(nums):
                return False
            if currSum > half:
                return False
            # if currSum + nums[n] > half:
            #     return False
            if currSum + nums[n] == half:
                return True

            if dp[n][currSum] is not None:
                return dp[n][currSum]
            
            skip = rec(n+1, currSum)
            take = rec(n+1, currSum + nums[n])
            if not skip and not take:
                dp[n][currSum] = False
            else:
                dp[n][currSum] = True
            return dp[n][currSum]
        return rec(0, 0)

                