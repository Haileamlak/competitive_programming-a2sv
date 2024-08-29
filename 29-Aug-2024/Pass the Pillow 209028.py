# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = time // (n - 1)
        remaining_time = time % (n - 1)

        if direction % 2 == 0:
            return 1 + remaining_time
        
        return n - remaining_time