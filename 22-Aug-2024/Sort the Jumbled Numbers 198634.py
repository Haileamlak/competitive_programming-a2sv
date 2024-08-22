# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def foo(x):
            temp = []
            for digit in str(x):
                temp.append(str(mapping[int(digit)]))
            
            return int(''.join(temp))
            
        nums.sort(key = foo)
        return nums