class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        nums.sort()
        def back_track(index):
            if index == len(nums):
                subsets.append(subset.copy())
                return
            
            next_index = index + 1
            while next_index < len(nums) and nums[index] == nums[next_index]: 
                next_index += 1
            
            subset.append(nums[index])
                
            back_track(index + 1)

            subset.pop()

            back_track(next_index)

        back_track(0)
        return subsets