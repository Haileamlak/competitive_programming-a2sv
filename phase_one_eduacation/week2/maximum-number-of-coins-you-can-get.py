class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        max_coins = 0
        for i in range(len(piles)//3):
            triplet = piles[len(piles) - 2 - (2 * i)]
            max_coins += triplet
                    
        return max_coins