class Solution:
    def totalMoney(self, n: int) -> int:
        dollars = [1, 2, 3, 4, 5, 6, 7]  
        dollar_sum = 7 * 8 // 2  
        quotient, remainder = divmod(n, 7)

        total = 0
        for i in range(quotient):
            total += dollar_sum + (7 * i)
        
        for i in range(remainder):
            total += dollars[i] + quotient

        return total

