# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        res = curr_cost = left = 0
        for right in range(n):
            curr_cost += abs(ord(s[right]) - ord(t[right]))

            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))

                left += 1
            
            res = max(res, right - left + 1)

        return res