# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        if m % 2 and n % 2:
            return reduce(xor, nums1) ^ reduce(xor, nums2)
        elif m % 2:
            return reduce(xor, nums2)
        elif n % 2:
            return reduce(xor, nums1)
        return 0