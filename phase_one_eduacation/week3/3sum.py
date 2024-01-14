class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n - 2:
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            
                elif temp < 0:
                    j += 1
                else:
                    k -= 1

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            i += 1
        return res