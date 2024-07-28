# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        result = 0

        unique = defaultdict(int)
        num_of_unique = 0

        left = 0
        for right in range(len(nums)):
            unique[nums[right]] += 1

            if unique[nums[right]] == 1:
                num_of_unique += 1

            while num_of_unique > k:
                unique[nums[left]] -= 1

                if unique[nums[left]] == 0:
                    del unique[nums[left]]
                    num_of_unique -= 1

                left += 1

            result += right - left + 1

        return result

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(
            nums, k
        ) - self.subarraysWithAtMostKDistinct(nums, k - 1)
