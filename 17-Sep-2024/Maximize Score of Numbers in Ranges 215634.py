# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def possible(x):
            curr = start[0]
            for i in range(1, len(start)):
                if curr + x < start[i]:
                    curr = start[i]
                elif curr + x > start[i] + d:
                    return False
                else:
                    curr = curr + x
            
            return True

        minn, maxx = 0, (10 ** 9) * 2
        while minn <= maxx:
            mid = minn + (maxx - minn) // 2
            if possible(mid):
                minn = mid + 1
            else:
                maxx = mid - 1

        return maxx