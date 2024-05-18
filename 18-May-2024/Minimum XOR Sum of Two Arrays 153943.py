# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)        

        @cache
        def get_min(i, mask):
            if i == n:
                return 0
            
            res = float('inf')
            for j in range(n):
                if not (mask & (1 << j)):
                    res = min(res, (nums1[i] ^ nums2[j]) + get_min(i + 1, mask | (1 << j)))
            
            return res
        
        return get_min(0, 0)