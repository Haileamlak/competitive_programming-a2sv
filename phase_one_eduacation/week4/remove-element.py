class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        placeholder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != val:
                nums[placeholder] = nums[seeker]
                placeholder += 1
            
            seeker += 1
        
        return placeholder