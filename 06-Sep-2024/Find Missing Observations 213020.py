# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing = mean * (n + m) - sum(rolls)
        if missing < n or ceil(missing / n) > 6:
            return []

        res = [missing // n for _ in range(n)]
        for i in range(missing % n):
            res[i] += 1

        return res