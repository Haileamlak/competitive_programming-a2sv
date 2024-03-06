# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            bad = left + (right - left) // 2

            if isBadVersion(bad):
                right = bad
            else:
                left = bad + 1
    

        return left