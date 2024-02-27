class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_weights = [0] * (len(weights) - 1)
        for i in range(len(weights) - 1):
            pair_weights[i] = weights[i] + weights[i + 1]

        pair_weights.sort()

        answer = 0
        for i in range(k - 1):
            answer += pair_weights[-1 - i] - pair_weights[i]
        
        return answer