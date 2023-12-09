class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = {}
        for i in range(len(matches)):
            winners.add(matches[i][0])
            losers[matches[i][1]] = losers.get(matches[i][1], 0) + 1

        answer = [[], []]
        for player in winners:
            if player not in losers:
                answer[0].append(player) 
        for player in losers:
            if losers[player] == 1:
                answer[1].append(player)

        answer[0].sort()
        answer[1].sort()
        return answer
