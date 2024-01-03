class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seeker = 1
        placeholder = 1
        while seeker < len(nums):
            if nums[seeker] != nums[seeker - 1]:
                nums[placeholder] = nums[seeker]
                placeholder += 1
            
            seeker += 1
        
        return placeholder

