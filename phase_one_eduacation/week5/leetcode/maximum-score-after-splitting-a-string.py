class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix_sum = [0 for _ in range(n)]

        prefix_sum[0] = int(s[0])

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + int(s[i])

        max_score = 0
        for i in range(0, n - 1):
            score = (i + 1 - prefix_sum[i]) + (prefix_sum[n - 1] - prefix_sum[i])
            max_score = max(score, max_score)

        return max_score