# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def can_divide(self, divisor, word):
        if len(word) % len(divisor) != 0:
            return False
            
        length = len(divisor)
        for i in range(len(word)):
            if word[i] != divisor[i % length]:
                return False

        return True
                
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        longest = gcd(n, m)

        divisor = list(str1[:longest])
        while len(divisor) != 0:
            if self.can_divide(divisor, str1) and self.can_divide(divisor, str2):
                return ''.join(divisor)
        
            divisor.pop()

        return ""