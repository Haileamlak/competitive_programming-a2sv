# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def binary_search(left, right):
            if left == right:
                return left

            mid = left + (right - left) // 2

            if isBadVersion(mid):
                return binary_search(left, mid)

            return binary_search(mid + 1, right)

        return binary_search(1, n)