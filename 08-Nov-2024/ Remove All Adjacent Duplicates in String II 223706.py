# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0], 1)]
        for i in range(1, len(s)):
            if not stack or s[i] != stack[-1][0]:
                stack.append((s[i], 1))
            else:
                stack.append((s[i], stack[-1][1] + 1))

            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
            
        return ''.join([tt[0] for tt in stack])