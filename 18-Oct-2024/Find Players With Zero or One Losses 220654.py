# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        lose_count = defaultdict(int)
        for winner, loser in matches:
            if winner not in lose_count:
                winners.add(winner)
            
            winners.discard(loser)
            lose_count[loser] += 1

        result = [list(sorted(winners)), sorted([loser for loser in lose_count if lose_count[loser] == 1])]
        return result

