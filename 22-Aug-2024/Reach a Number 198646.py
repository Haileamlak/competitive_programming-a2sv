# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        if target == 2:
            return 3
        
        res = 0
        ans = 0
        while res < target:
            ans += 1
            res += ans
        
        if (res - target) % 2 == 0:
            return ans

        ans += 1
        res += ans
        if (res - target) % 2 == 0:
            return ans

        return ans + 1