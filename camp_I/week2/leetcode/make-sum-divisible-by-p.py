class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        index = {0:-1}
        total = sum(nums)
        
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i - 1]

        res = len(nums)
        rem = total % p
        currSum =0

        if rem == 0:
            return 0

        for i in range(len(nums)):
            currSum += nums[i]
            rem2 = currSum % p

            target = (rem2 - rem) % p
            if rem2 == rem:
                res = min(res, i + 1)
                
            if target in index:
                res = min(res, i - index[target])

            # if p + rem2 - rem in index:
            #     res = min(res, i - index[p + rem2 - rem])
            
            index[rem2] = i
        
        if res == len(nums):
            return -1

        return res