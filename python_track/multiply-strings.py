class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        for i in range(len(num1)):
            int_num1 += int(num1[len(num1) - 1 - i]) * (10 ** i)
        int_num2 = 0
        for i in range(len(num2)):
            int_num2 += int(num2[len(num2) - 1 - i]) * (10 ** i)
        
        return str(int_num1 * int_num2)
