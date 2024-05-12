# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        
        @cache
        def foo(row, col, k):
            if row < 0 or row >= n or col < 0 or col >= n:
                return 0
            
            if k == 0:
                return 1

            res = 0
            for i, j in directions:
                r, c = row + i, col + j
                res += foo(r, c, k - 1)
            
            return res
        
        return foo(row, column, k) / (8 ** k)