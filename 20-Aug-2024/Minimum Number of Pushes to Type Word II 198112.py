# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        res = 0
        pushes = 1
        current = 1
        for value in sorted(count.values(), reverse = True):
            res += value * pushes
            current += 1
            
            if current == 9:
                current = 1
                pushes += 1
            
        return res