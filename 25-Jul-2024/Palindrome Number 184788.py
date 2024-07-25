# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp_x = x
        x_reversed = 0
        while temp_x:
            x_reversed *=10
            x_reversed += temp_x % 10
            temp_x //= 10

        return x == x_reversed