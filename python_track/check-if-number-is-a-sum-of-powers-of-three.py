class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n > 0):
            if(n % 3 == 2):
                return 
            n //= 3
        
        return True