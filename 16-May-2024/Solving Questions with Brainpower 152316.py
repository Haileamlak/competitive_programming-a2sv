# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            pick = questions[i][0]

            index = i + questions[i][1] + 1
            if index < n:
                pick += dp[index]

            not_pick = dp[i + 1]

            dp[i] = max(pick, not_pick)
        
        return dp[0]