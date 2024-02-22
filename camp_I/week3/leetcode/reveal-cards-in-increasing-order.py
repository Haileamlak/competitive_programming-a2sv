class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque(range(len(deck)))
        res = [0] * len(deck)
        deck.sort()

        for card in deck:
            index = queue.popleft()

            res[index] = card
            
            if queue:
                queue.append(queue.popleft())
            
        return res
