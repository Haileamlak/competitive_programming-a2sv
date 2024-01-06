class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        i = 0
        n = len(nums)
        while i < n - 2:
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(target - temp) < abs(target - res):
                    res = temp
                # if temp == target:
                #     return target
                if target - temp > 0:
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    j += 1
                else: 
                    while k > j and nums[k] == nums[k - 1]: k -= 1
                    k -= 1
            
            while i < n - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return res

        