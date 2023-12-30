class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def isLarger(a, b):
            for i in range(max(len(a), len(b))):
                if i == len(a):
                    return isLarger(a, b[i:])
                elif i == len(b):
                    return isLarger(a[i:], b)
                elif a[i] != b[i]:
                        return a[i] > b[i]

            return False

        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(1, len(nums) - i):
                if isLarger(nums[j], nums[j - 1]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        if nums[0] == '0':
            return '0'
        return ''.join(nums)