# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        def counting_sort(arr, n, exp):
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                count[(arr[i] // exp) % 10] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                output[count[(arr[i] // exp) % 10] - 1] = arr[i]
                count[(arr[i] // exp) % 10] -= 1

            for i in range(n):
                arr[i] = output[i]

        maxx = max(nums)
        exp = 1
        n = len(nums)
        while exp <= maxx:
            counting_sort(nums, n, exp)
            exp *= 10

        return max(
            nums[i] - nums[i - 1] for i in range(1, n)
        )