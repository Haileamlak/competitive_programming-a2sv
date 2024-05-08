# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p = len(players) - 1
        t = len(trainers) - 1
        
        count = 0 
        
        while(p >= 0 and t >= 0):
            if players[p] <= trainers[t]:
                count+=1
                p-=1
                t-=1
            else:
                p-=1 
        
        return count