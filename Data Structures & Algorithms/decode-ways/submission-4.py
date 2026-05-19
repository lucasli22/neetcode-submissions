class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)

        def rec(n):
            if n == len(s):
                return 1
            if dp[n] != -1:
                return dp[n]
            if s[n] == "0":
                return 0 
            dp[n] = rec(n+1)
            if n < len(s) - 1:
                if s[n] != "0" and 10 <= int(s[n:n+2]) <= 26:
                    dp[n] += rec(n + 2)
                
            return dp[n]

        
        return rec(0)