class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left = 0
        totalUnique = 0
        unique_set = set()
        for num in nums:
            if num not in unique_set:
                totalUnique += 1
                unique_set.add(num)
            # else:
        
        print(totalUnique)
        res = 0
        window = defaultdict(int)
        curr_unique = 0
        right = -1
        while right < len(nums):
            if curr_unique == totalUnique:
                res += len(nums) - right
                print('res', res)
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    curr_unique -= 1
                    del window[nums[left]]
                print(curr_unique)
                left += 1
            else:
                right += 1
                if right == len(nums):
                    break
                window[nums[right]] += 1
                if window[nums[right]] == 1:
                    curr_unique += 1
                    # window.add(nums[right])
                # else:
                
        
        return res
            