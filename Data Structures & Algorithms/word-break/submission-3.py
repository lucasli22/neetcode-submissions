class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        idx = 0
        self.status = False
        dp = [False] * len(s)
        def rec(n):
            if n >= len(s):
                self.status = True
                return
            if dp[n] == True:
                return
            for word in wordDict:
                if s[n:n+len(word)] == word:
                    dp[n] = True
                    rec(n+len(word))
        rec(0)
        return self.status
        