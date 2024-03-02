class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        tempx = x
        x_reversed = 0
        while tempx:
            x_reversed *=10
            x_reversed += tempx % 10
            tempx //= 10

        return x == x_reversed