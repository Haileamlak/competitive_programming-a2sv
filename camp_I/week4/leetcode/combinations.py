class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        combination = []

        def backtrack(i):
            if len(combination) == k:
                answer.append(combination.copy())
                return
            
            for number in range(i + 1, n + 1):
                combination.append(number)

                backtrack(number)
            
                combination.pop()
        
        backtrack(0)
        return answer