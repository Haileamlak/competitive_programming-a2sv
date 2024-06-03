# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        i = 0
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                
                if triplet_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])

                if triplet_sum <= 0:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    j += 1

                if triplet_sum >= 0:
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    k -= 1

            while i < n - 2 and nums[i] == nums[i + 1]:
                i += 1
        
            i += 1

        return res