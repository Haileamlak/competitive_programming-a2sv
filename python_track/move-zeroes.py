class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0
        
        while read < len(nums):
            if nums[read] != 0:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write += 1
            # else:
            #     write = read

            read += 1