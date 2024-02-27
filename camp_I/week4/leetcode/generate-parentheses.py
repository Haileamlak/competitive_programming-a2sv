class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        answer = []
        def backtrack(openings, closings):
            if len(combination) == 2 * n:
                answer.append(''.join(combination))
            
            if openings < n:
                combination.append('(')
                backtrack(openings + 1, closings)
                combination.pop()
            
            if closings < openings:
                combination.append(')')
                backtrack(openings, closings + 1)
                combination.pop()
        
        backtrack(0, 0)

        return answer