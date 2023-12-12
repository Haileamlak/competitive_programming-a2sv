class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in nums_index and nums_index[num2] != i:
                return [i, nums_index[num2]]
            
            nums_index[nums[i]] = i
        
        
