# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """     
        count = [0, 0, 0] # [red, white, blue]

        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(3):
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1