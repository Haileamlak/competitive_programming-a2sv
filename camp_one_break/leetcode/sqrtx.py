class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        while left <= (right):
            mid = left + (right - left) // 2
            if mid < x // mid:
                left = mid + 1
            elif mid > x // mid:
                right = mid - 1
            else:
                return mid

        return right