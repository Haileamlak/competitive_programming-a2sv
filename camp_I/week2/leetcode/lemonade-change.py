class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr5 = 0
        curr10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                curr5 += 5
            elif bills[i] == 10:
                curr5 -= 5
                curr10 += 10
            else:
                if curr10:
                    curr10 -= 10
                    curr5 -= 5
                else:
                    curr5 -= 15

            if curr5 < 0:
                return False
        
        return True