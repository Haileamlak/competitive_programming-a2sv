# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map(x):
            if x == 0:
                return mapping[0]

            place = 1
            res = 0
            while x:
                res = place * mapping[x % 10] + res
                x //= 10
                place *= 10
            
            return res
            
        nums.sort(key = map)
        return nums