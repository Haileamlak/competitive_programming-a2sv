class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        index = {nums[0] % p:0}
        total = sum(nums)
        # if (total - nums[0]) % p == 0:
        #     return 1
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        # for i in range(1, len(nums)):
        #     temp = p - ((total - nums[i]) % p)
        
        res = len(nums)
        rem = total % p
        for i in range(len(nums)):
            rem2 = nums[i] % p

            if rem2 == rem:
                res = min(res, i + 1)
            if rem2 - rem in index:
                res = min(res, i - index[rem2 - rem])

            if p + rem2 - rem in index:
                res = min(res, i - index[p + rem2 - rem])
            
            index[nums[i] % p] = i

            # if (p - (nums[i] % p)) in index:
            #     res = min(res, i - index[p - nums[i] % p] + 1)
            
        
        if res == len(nums):
            return -1

        return res