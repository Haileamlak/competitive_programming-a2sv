# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x = pow(5, ceil(n / 2), (pow(10, 9) + 7)) * pow(4, (n // 2), (pow(10, 9) + 7))

        return x % (pow(10, 9) + 7)