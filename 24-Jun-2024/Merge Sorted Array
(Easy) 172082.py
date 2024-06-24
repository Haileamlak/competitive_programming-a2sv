# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        placeholder = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[placeholder] = nums1[i]
                i -= 1
            else:
                nums1[placeholder] = nums2[j]
                j -= 1
            
            placeholder -= 1
        
        while j >= 0:
            nums1[placeholder] = nums2[j]
            
            j -= 1
            placeholder -= 1