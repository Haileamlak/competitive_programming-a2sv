class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        less = 0
        for i in range(1, len(nums)):
            if nums[i] > res:
                target = nums[i] - res
                if target <= less:
                    less -= target
                    target = 0
                else:
                    target -= less
                    less = 0
                
                res += ceil(target / (i + 1))
                if (target % (i + 1)):
                    less += (i + 1) - (target % (i + 1))
            else:
                less += res - nums[i]
                
        return res