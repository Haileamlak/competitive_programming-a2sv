class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # count of unique numbers inside nums
        totalUnique = len(set(nums))

        # the output initially is zero
        res = 0

        # count of each number in the window currently
        window = defaultdict(int)

        # count of unique numbers currently inside the window
        curr_unique = 0

        left = 0
        for right in range(len(nums)):
            window[nums[right]] += 1
            if window[nums[right]] == 1:
                curr_unique += 1

            while curr_unique == totalUnique:
                res += len(nums) - right # if it works for right it should work also for all indexes greater than right

                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    curr_unique -= 1
                    del window[nums[left]]

                left += 1
        
        return res
            