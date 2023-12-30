class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = [ch for ch in str(num)]
        nums.sort()

        if nums[0] == '-':
            nums = sorted(nums[1:], reverse=True)

            return -1 * int(''.join(nums))
        
        nums.sort()
        if nums[0] == '0' and len(nums) > 1:
            j = 0
            while nums[j] == '0':
                j += 1
            
            nums[0], nums[j] = nums[j], nums[0]

        return int(''.join(nums))
        #     for i in range(1, len(nums)):
        #         for j in range(2, len(nums) - i + 1):
        #             if nums[j - 1] < nums[j]:
        #                 nums[j], nums[j - 1] = nums[j - 1], nums[j]

        # else:
        #     for i in range(len(nums)):
        #         for j in range(1, len(nums) - i):
        #             if j == 1 and nums[j] == '0':
        #                 pass
        #             elif nums[j - 1] > nums[j]:
        #                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
        
        # return int(''.join(nums))