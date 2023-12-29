class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max1 = max(nums1)
        count1 = [0 for _ in range(max1 + 1)]
        for num in nums1:
            count1[num] += 1
        
        max2 = max(nums2)
        count2 = [0 for _ in range(max2 + 1)]
        for num in nums2:
            count2[num] += 1

        res = []
        length = min(max1, max2)
        for i in range(length + 1):
            j = min(count1[i], count2[i])
            while j > 0:
                res.append(i)
                j -= 1
        
        return res