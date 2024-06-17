# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(start, end, number):
            if start > end:
                return False
            
            mid = start + (end - start) // 2
            if mid * mid == number:
                return True
            
            if mid * mid < number:
                return binary_search(mid + 1, end, number)
            
            return binary_search(start, mid - 1, number)
            
        for a in range(int((sqrt(c)) + 1)):
            b = c - (a * a)
            if int(sqrt(b)) == sqrt(b):
                return True
            
        return False