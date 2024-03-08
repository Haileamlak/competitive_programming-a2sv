class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 0, x
        while int(left) < int(right):
            mid = left + (right - left) / 2
            if mid < x / mid:
                left = mid
            elif mid > x / mid:
                right = mid
            else:
                return int(mid)

        return int(left)