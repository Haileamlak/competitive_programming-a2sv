class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k -= 1
        friends = [i for i in range(1, n + 1)]
        index = 0
        start = 0
        
        while n > 1:
            start = (start + k) % n
            friends.pop(start)

            n -= 1
        
        return friends[0]