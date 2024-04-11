# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i = 0
        while i < len(num):
            while stack and num[i] < stack[-1] and k:
                stack.pop()
                k -= 1

            stack.append(num[i])
            i += 1

        while k and stack:
            stack.pop()
            k -= 1

        return max((''.join(stack) + num[i:]).lstrip('0'), '0')