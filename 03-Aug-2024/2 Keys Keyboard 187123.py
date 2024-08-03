# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        dp = {1: 0}

        def minStepsHelper(n):
            if n in dp:
                return dp[n]

            res = n
            
            for i in range(2, n):
                if n % i == 0:
                    res = min(res, i + minStepsHelper(n // i))

            dp[n] = res

            return res

        return minStepsHelper(n)