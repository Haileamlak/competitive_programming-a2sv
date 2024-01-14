class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0

        curr = 0 # current sum of the window
        window = set() # current elements in the window
        left = 0
        for right in range(len(nums)):
            while nums[right] in window:
                curr -= nums[left]
                window.remove(nums[left])
                left += 1

            window.add(nums[right])
            curr += nums[right]

            res = max(res, curr)

        return res 