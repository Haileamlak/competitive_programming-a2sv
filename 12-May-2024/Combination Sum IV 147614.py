# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def foo(_sum):
            if _sum > target:
                return 0

            if _sum == target:
                return 1
            
            res = 0
            for num in nums:
                res += foo(_sum + num)

            return res

        return foo(0)