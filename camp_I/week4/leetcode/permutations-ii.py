class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        combination = []
        visited = set()

        def backtrack():
            if len(combination) == len(nums):
                res.add(tuple(combination))
                return
                
            for i in range(len(nums)):
                if i not in visited:
                    combination.append(nums[i])
                    visited.add(i)
                    backtrack()
                    visited.remove(i)
                    combination.pop()

        backtrack()

        return list(res)