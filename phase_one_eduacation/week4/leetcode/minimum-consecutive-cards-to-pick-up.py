class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = len(cards) + 1
        left = 0
        window = set()
        for right in range(len(cards)):
            while cards[right] in window:
                window.remove(cards[left])
                left += 1
            
            window.add(cards[right])
    
            if left > 0:
                res = min(res, right - left + 2)
        
        if res > len(cards):
            return -1
        return res