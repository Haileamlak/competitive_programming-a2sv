# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        dp = [[False] * (len(t) + 1) for _ in range(len(s) + 1)]
        for col in range(len(t) + 1):
            dp[0][col] = True
        
        for row in range(1, len(s) + 1):
            for col in range(1, len(t) + 1):
                
                dp[row][col] = s[row - 1] == t[col - 1] or dp[row][col - 1]
                dp[row][col] = dp[row][col] and dp[row - 1][col - 1]
        
        return dp[-1][-1]