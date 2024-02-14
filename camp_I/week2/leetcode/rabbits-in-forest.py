class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = len(answers)
        for answer in count.keys():
            count[answer] %= answer + 1

            if count[answer] != 0:
                res += answer - count[answer] + 1
        
        return res