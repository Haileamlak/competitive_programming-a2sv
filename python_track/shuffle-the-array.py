class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        n = len(nums) // 2
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[n + i]) 
        
        return shuffled
