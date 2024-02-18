class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = deque()
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in operators:
                num1 = result.pop()
                num2 = result.pop()
                res = 0
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num2 - num1
                elif token == '*':
                    res = num1 * num2
                else: # token == '/'
                    res = int(num2 / num1)

                result.append(res)
            
            else:
                result.append(int(token))  
        
        return result[0]