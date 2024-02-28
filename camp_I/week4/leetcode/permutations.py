class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        def back_track(index):
            nonlocal permutations, permutation
            if index == len(nums):
                permutations.append(permutation.copy())
                return
            
            for i in range(index, len(nums)):
                permutation.append(nums[i])
                nums[i], nums[index] = nums[index], nums[i]
                back_track(index + 1)
                permutation.pop()
                nums[i], nums[index] = nums[index], nums[i]
        
        back_track(0)

        return permutations