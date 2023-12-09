class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        isPositive = True
        pos = 0
        neg = 0

        while len(res) < len(nums):
            if isPositive:
                while nums[pos] < 0:
                    pos += 1                
                res.append(nums[pos])
                pos += 1
                isPositive = False

            else:
                while nums[neg] > 0:
                    neg += 1
                res.append(nums[neg])
                neg += 1
                isPositive = True

        return res