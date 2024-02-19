class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {}
        for i in range(len(nums1)):
            index_map[nums1[i]] = i
        
        res = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                number = stack[-1]
                if number in index_map:
                    res[index_map[number]] = num
                stack.pop()

            stack.append((num))
        
        return res