class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        subsets = []
        def back_track(index):
            subsets.append(subset.copy())
            for i in range(index + 1, len(nums)):
                subset.append(nums[i])
                back_track(i)
                subset.pop()
        
        back_track(-1)
        return subsets