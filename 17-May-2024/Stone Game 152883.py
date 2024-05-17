# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def play(start, end, is_alice):
            if start == end:
                if is_alice:
                    return piles[start]
                
                return -piles[start]

            if is_alice:
                return max(piles[start] + play(start + 1, end, False), piles[end] + play(start, end - 1, False))
            
            return min(-piles[start] + play(start + 1, end, True), -piles[end] + play(start, end - 1, True))
        
        return play(0, len(piles) - 1, True) > 0