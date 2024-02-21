class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for bracket in s:
            if bracket == '(':
                stack.append('(')
            
            else:
                inside = 0
                while stack[-1] != '(':
                    inside += stack[-1]
                    stack.pop()
                
                result = 1
                if inside:
                    result = inside * 2

                stack.pop()
                
                stack.append(result)
        
        
        return sum(stack)

