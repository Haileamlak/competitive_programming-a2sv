class Solution:
    def minOperations(self, s: str) -> int:
        min0 = 0

        for i in range(len(s)):
            if i % 2 == 0 and s[i] != "0":
                min0 += 1
            elif i % 2 == 1 and s[i] != "1":
                min0 += 1
        
        min1 = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != "1":
                min1 += 1
            elif i % 2 == 1 and s[i] != "0":
                min1 += 1

        return min(min0, min1)