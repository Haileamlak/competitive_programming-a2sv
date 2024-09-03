# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        count = Counter(nums)
        taken = []
        
        moves = 0
        for x in range(len(nums) + max_val):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                moves += x - taken.pop()
                
        return moves