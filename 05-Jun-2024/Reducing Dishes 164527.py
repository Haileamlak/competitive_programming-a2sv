# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        @cache
        def foo(i, j):
            if i == n:
                return 0
            
            return max(
                satisfaction[i] * j + foo(i + 1, j + 1),
                foo(i + 1, j)
            )
        
        return foo(0, 1)