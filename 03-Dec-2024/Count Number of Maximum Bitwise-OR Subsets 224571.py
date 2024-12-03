# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def func(x, y):
            return x | y

        max_or = reduce(func, nums)

        res = 0
        for mask in range(2 ** len(nums)):
            curr = 0
            for i in range(len(nums)):
                if mask & (1 << i):
                    curr |= nums[i]
                
            if curr == max_or:
                res += 1

        return res