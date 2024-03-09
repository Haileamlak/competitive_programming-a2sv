class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        top = bottom = 0

        while top < len(nums1) and bottom < len(nums2):
            if nums1[top] < nums2[bottom]:
                top += 1
            elif nums2[bottom] < nums1[top]:
                bottom += 1
            else:
                return nums1[top]
        
        return -1