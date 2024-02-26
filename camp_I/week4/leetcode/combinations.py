class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        stack = []

        def backtrack(i):
            if len(stack) == k:
                answer.append(stack.copy())
                return
            
            for j in range(i + 1, n + 1):
                stack.append(j)

                backtrack(j)
            
                stack.pop()
        
        backtrack(0)
        return answer
