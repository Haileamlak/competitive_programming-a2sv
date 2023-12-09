class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        
        return less + equal + greater

        # left = 0
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         nums[i], nums[left] = nums[left], nums[i]
        #         left += 1

        # right = len(nums) - 1
        # for i in range(len(nums) - 1, left - 1, -1):
        #     if nums[i] > pivot:
        #         nums[i], nums[right] = nums[right], nums[i]
        #         right -= 1
            
        # return nums