class Solution:
    def isValid(self, s: str) -> bool:
        closing_bracket = {')':'(', ']':'[', '}':'{'}
        stack = []
        for bracket in s:
            if bracket in closing_bracket:
                if not len(stack) or stack[-1] != closing_bracket[bracket]:
                    return False
                stack.pop()
                
            else:
                stack.append(bracket)
        
        return not len(stack)         