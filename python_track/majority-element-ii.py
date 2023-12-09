class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = []
        n = len(nums) // 3
        for key in count:
            if count[key] > n:
                res.append(key)

        return res