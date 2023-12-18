class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n!= 1:
            if n in nums:
                return False
            
            nums.add(n)
            num = 0
            while n != 0:
                num += pow(n % 10, 2)
                n //= 10  
                
            n = num
        
        return True
        
            
