# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        for i in range(1, len(str1) + 1):
            if len(str1) % i != 0:
                continue

            x = str1[:i]
            if x * (len(str1) // i) == str1 and x * (len(str2) // i) == str2:
                res = x

        return res