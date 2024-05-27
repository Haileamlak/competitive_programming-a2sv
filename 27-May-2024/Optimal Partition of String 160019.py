# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        curr = set()
        for letter in s:
            if letter in curr:
                res += 1
                curr = set([letter])
            else:
                curr.add(letter)
        
        return res