class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        top = 0
        bottom = 0
        while top < len(nums1) and bottom < len(nums2):
            if nums1[top] == nums2[bottom]:
                return nums1[top]
            elif nums1[top] < nums2[bottom]:
                top += 1
            else:
                bottom += 1   

        return -1     