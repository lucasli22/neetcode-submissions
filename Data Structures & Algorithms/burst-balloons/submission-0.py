class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] = max(dp[i][k] + dp[k][j] + )
        n = len(nums)
        dp = [[0] * (n) for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j + 1):
                    if i - 1 >= 0:
                        left = nums[i - 1]
                    else:
                        left = 1

                    if j + 1 < n:
                        right = nums[j + 1]
                    else:
                        right = 1
                    coins = left * right * nums[k]
                    leftCoin = dp[i][k - 1] if k > i else 0
                    rightCoin = dp[k + 1][j] if k < j else 0
                    dp[i][j] = max(dp[i][j], leftCoin + rightCoin+ coins)

        return dp[0][n - 1]