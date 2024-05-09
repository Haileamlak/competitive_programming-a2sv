# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1

        res = 0
        mask = 0
        for letter in word:
            pos = ord(letter) - ord('a')
            mask ^= (1 << pos)

            res += count[mask]

            for i in range(10):
                res += count[mask ^ (1 << i)]

            count[mask] += 1
        
        return res