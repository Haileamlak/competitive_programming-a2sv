class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        splitting = [0] * (len(weights) - 1)
        for i in range(len(weights) - 1):
            splitting[i] = weights[i] + weights[i + 1]
            
        splitting.sort()

        min_score = max_score = weights[0] + weights[-1]
        for i in range(k - 1):
            min_score += splitting[i]
            max_score += splitting[-1 - i]
        
        return max_score - min_score