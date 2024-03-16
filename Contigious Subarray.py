class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        temp = {0:-1}
        curr = 0
        res = 0
        for i in range(len(nums)):
            if nums[i]:
                curr += 1
            else:
                curr -= 1
            
            if curr in temp:
                res = max(res, i - temp[curr])
            else:
                temp[curr] = i
        
        return res
