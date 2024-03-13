class Solution:
    def pivotInteger(self, n: int) -> int:
        n_sum = (n * (n + 1) // 2)
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            l_sum = (mid * (mid + 1) // 2)
            r_sum = n_sum - l_sum + mid
            if l_sum < r_sum:
                left = mid + 1
            elif r_sum < l_sum:
                right = mid - 1
            else:
                return mid
        
        return -1