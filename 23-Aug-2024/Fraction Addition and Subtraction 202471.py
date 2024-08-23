# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        if len(expression) <= 4:
            return expression

        if expression[0] != "-":
            expression = '+' + expression

        n = len(expression)

        nums = numbers = list(map(int, re.findall(r'[+-]?\d+', expression)))

        numerators = [nums[i] for i in range(0, len(nums), 2)]
        denominators = [nums[i] for i in range(1, len(nums), 2)]

        def mult(x, y):
            return x * y

        gcdd = reduce(gcd, denominators)
        lcmm = reduce(mult, denominators) // gcdd
        ans = 0
        for i in range(len(numerators)):
            ans += numerators[i] * (lcmm // denominators[i])
        
        x = gcd(ans, lcmm)
        return str(ans // x) + '/' + str(lcmm // x)