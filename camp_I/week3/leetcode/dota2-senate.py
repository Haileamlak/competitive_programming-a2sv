class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        banned_dire = 0
        banned_radiant = 0
        queue = deque(senate)
        while count['R'] and count['D']:
            senator = queue.popleft() 
            if senator == 'D' and banned_dire:
                banned_dire -= 1
            elif senator == 'D':
                banned_radiant += 1
                count['R'] -= 1
                queue.append(senator)
            elif banned_radiant:
                banned_radiant -= 1
            else:
                banned_dire += 1
                count['D'] -= 1
                queue.append(senator)

        if count['R']:
            return 'Radiant'
        
        return 'Dire'