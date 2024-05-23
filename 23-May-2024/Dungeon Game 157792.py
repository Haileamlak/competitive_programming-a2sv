# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @cache
        def foo(row, col):
            if row == m - 1 and col == n - 1:
                return -min(0, dungeon[row][col])
                
            if row >= m or col >= n:
                return float('inf')

            res = dungeon[row][col] - min(foo(row + 1, col), foo(row, col + 1))
            return -min(0, res)
            
        return foo(0, 0) + 1