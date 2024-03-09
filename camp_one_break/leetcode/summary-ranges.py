class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
            
        start = end = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - end == 1:
                end = nums[i]
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + '->' + str(end))
                start = end = nums[i]
        
        if start == end: 
            res.append(str(start))
        else:
            res.append(str(start) + '->' + str(end))

        return res