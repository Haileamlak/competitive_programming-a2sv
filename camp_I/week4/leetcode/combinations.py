class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        combination = []

        def backtrack(number):
            if len(combination) == k:
                answer.append(combination.copy())
                return
            
            if number == n + 1:
                return
            
            combination.append(number)

            backtrack(number + 1)
        
            combination.pop()

            backtrack(number + 1)
        
        backtrack(1)
        return answer