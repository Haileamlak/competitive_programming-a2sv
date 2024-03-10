class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        res = set()
        for num in nums2:
            index = bisect_left(nums1, num)
            if index != len(nums1) and nums1[index] == num:
                res.add(num)

        return list(res)