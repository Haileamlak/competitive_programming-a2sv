# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False

        n = len(stones)

        def binary_search(left, right, stone):
            while left <= right:
                mid = left + (right - left) // 2
                if stones[mid] <= stone:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return right

        @cache
        def can_cross(i, k):
            if i == n - 1:
                return True

            if i >= n:
                return False

            next_stone1 = binary_search(i + 1, n - 1, stones[i] + k + 1)
            if i < next_stone1 < n and stones[next_stone1] == stones[i] + k + 1:
                if can_cross(next_stone1, k + 1):
                    return True
            
            next_stone2 = binary_search(i + 1, n - 1, stones[i] + k)
            if i < next_stone2 < n and stones[next_stone2] == stones[i] + k:
                if can_cross(next_stone2, k):
                    return True
            
            if k > 1:
                next_stone3 = binary_search(i + 1, n - 1, stones[i] + k - 1)
                if i < next_stone3 < n and stones[next_stone3] == stones[i] + k - 1:
                    if can_cross(next_stone3, k - 1):
                        return True
            
            return False

        return can_cross(1, 1)