# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res_set = set()
        result_stack = []
        unexplored = Counter(s)
        for ch in s:
            if ch not in res_set:
                while result_stack and ch < result_stack[-1] and result_stack[-1] in unexplored:
                    res_set.remove(result_stack[-1])
                    result_stack.pop()
                
                result_stack.append(ch)
                res_set.add(ch)
            
            unexplored[ch] -= 1
            if unexplored[ch] == 0:
                del unexplored[ch]
        
        return ''.join(result_stack)