class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if(n == 1):
            return 2
        
        x = n
        while(True):
            if(x % 2 == 0 and x % n == 0):
                return x
            x += 1